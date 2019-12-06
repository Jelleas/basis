grammar Basis;

tokens { INDENT, DEDENT }

// Thanks! https://issue.life/questions/43622514
@lexer::members {

    # A queue where extra tokens are pushed on (see the NEWLINE lexer rule).
    self.tokens = []

    # The stack that keeps track of the indentation level.
    self.indents = []

    # The amount of opened braces, brackets and parenthesis.
    self.opened = 0

    # The most recently produced token.
    self.last_token = None

def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    if self._input.LA(1) == Token.EOF and len(self.indents) > 0:
        # Remove any trailing EOF tokens from our buffer.
        while len(self.tokens) > 0 and self.tokens[-1].type == Token.EOF:
            del self.tokens[-1]

        # First emit an extra line break that serves as the end of the statement.
        self.emitToken(self.common_token(BasisLexer.NEWLINE, "\n"));

        # Now emit as much DEDENT tokens as needed.
        while len(self.indents) != 0:
            self.emitToken(self.create_dedent())
            del self.indents[-1]

        # Put the EOF back on the token stream.
        self.emitToken(self.common_token(Token.EOF, "<EOF>"));

    next = super().nextToken();

    if next.channel == Token.DEFAULT_CHANNEL:
        # Keep track of the last token on the default channel.
        self.last_token = next

    if len(self.tokens) == 0:
        return next
    else:
        t = self.tokens[0]
        del self.tokens[0]
        return t

def create_dedent(self):
    from lang.BasisParser import BasisParser
    dedent = self.common_token(BasisParser.DEDENT, "")
    dedent.line = self.last_token.line
    return dedent

def common_token(self, _type,  text):
    from antlr4.Token import CommonToken
    stop = self.getCharIndex() - 1
    if len(self.text) == 0:
        start = stop
    else:
        start = stop - len(self.text) + 1
    return CommonToken(self._tokenFactorySourcePair, _type, Lexer.DEFAULT_TOKEN_CHANNEL, start, stop)

## Calculates the indentation of the provided spaces, taking the
## following rules into account:
##
## "Tabs are replaced (from left to right) by one to eight spaces
##  such that the total number of characters up to and including
##  the replacement is a multiple of eight [...]"
##
##  -- https://docs.python.org/3.1/reference/lexical_analysis.html#indentation
def getIndentationCount(self, spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count

def atStartOfInput(self):
    return self._interp.column == 0 and self._interp.line == 1

}


start
   : (NEWLINE | statement)* EOF
   ;

statement
   : expression
   | comparison
   | assignment
   | if_statement
   | for_statement
   | while_statement
   | do_while_statement
   | function_definition
   ;

block
   : NEWLINE INDENT (statement (NEWLINE)?)+ DEDENT
   ;

function_definition
   : 'function' variable LPAREN parameter_list RPAREN block
   ;

parameter_list
   : variable
   | parameter_list ',' variable
   ;

function_call
   : variable LPAREN argument_list RPAREN
   ;

argument_list
   : comparison
   | argument_list ',' comparison
   ;

if_statement
   : 'if' comparison block ('else' block)?
   | 'if' comparison block ('else' if_statement)?
   ;

while_statement
   : 'while' comparison block
   ;

do_while_statement
   : 'do' block 'while' comparison
   ;

for_statement
   : 'for' LPAREN for_expression? ';' for_expression? ';' for_expression? RPAREN block
   ;

for_expression
   : assignment
   | comparison
   | for_expression ',' assignment
   | for_expression ',' comparison
   ;

assignment
   : variable EQ comparison
   ;

comparison
   : then_comparison ((DUBEQ | NEQ) then_comparison)*
   | then_comparison
   ;

then_comparison
   : not_comparison ((LT | GT | GET | LET) not_comparison)*
   | not_comparison
   ;

not_comparison
   : NOT not_comparison
   | expression
   ;

expression
   : term ((PLUS | MINUS) term)*
   ;

term
   : factor ((TIMES | DIV) factor)*
   ;

factor
   : signedAtom (POW signedAtom)*
   ;

signedAtom
   : PLUS signedAtom
   | MINUS signedAtom
   | atom
   ;

atom
   : literal
   | function_call
   | variable
   | LPAREN comparison RPAREN
   ;

literal
   : NUMBER
   | BOOL
   ;

variable
   : VARIABLE
   ;


BOOL
   : 'true'
   | 'True'
   | 'false'
   | 'False'
   ;


NUMBER
   : ('0' .. '9') + ('.' ('0' .. '9') +)?
   ;


fragment E
   : 'E' | 'e'
   ;


fragment SIGN
   : ('+' | '-')
   ;


LPAREN
   : '('
   ;


RPAREN
   : ')'
   ;


PLUS
   : '+'
   ;


MINUS
   : '-'
   ;


TIMES
   : '*'
   ;


DIV
   : '/'
   ;


NOT
   : '!'
   ;


GT
   : '>'
   ;


LT
   : '<'
   ;


GET
   : '>='
   ;


LET
   : '<='
   ;


DUBEQ
   : '=='
   ;


EQ
   : '='
   ;


NEQ
   : '!='
   ;


POINT
   : '.'
   ;


POW
   : '^'
   ;


VARIABLE
  : VALID_ID_START VALID_ID_CHAR*
  ;


fragment VALID_ID_START
  : ('a' .. 'z') | ('A' .. 'Z') | '_'
  ;


fragment VALID_ID_CHAR
  : VALID_ID_START | ('0' .. '9')
  ;


fragment SPACES
   : [ \t]+
   ;


NEWLINE
: ( {self.atStartOfInput()}?   SPACES
  | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
  )

  {
   import re
   from lang.BasisParser import BasisParser
   new_line = re.sub(r"[^\r\n\f]+", "", self._interp.getText(self._input)) #.replaceAll("[^\r\n\f]+", "")
   spaces = re.sub(r"[\r\n\f]+", "", self._interp.getText(self._input)) #.replaceAll("[\r\n\f]+", "")
   next = self._input.LA(1)

   if self.opened > 0 or next == '\r' or next == '\n' or next == '\f' or next == '#':
       self.skip()
   else:
       self.emitToken(self.common_token(BasisParser.NEWLINE, new_line))

       indent = self.getIndentationCount(spaces)
       if len(self.indents) == 0:
           previous = 0
       else:
           previous = self.indents[-1]

       if indent == previous:
           self.skip()
       elif indent > previous:
           self.indents.append(indent)
           self.emitToken(self.common_token(BasisParser.INDENT, spaces))
       else:
           while len(self.indents) > 0 and self.indents[-1] > indent:
               self.emitToken(self.create_dedent())
               del self.indents[-1]

  };


WS
   : [ \t] + -> skip
   ;
