grammar Basis;

start
   : sequence
   ;

sequence
   : statement (NEWLINE statement)*
   ;

statement
   : expression
   | comparison
   | assignment
   ;

assignment
   : variable EQ expression
   | variable EQ comparison
   ;

comparison
   : expression relop expression
   ;

expression
   : term ((PLUS | MINUS) term)*
   | variable
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
   | variable
   | LPAREN expression RPAREN
   ;

literal
   : LITERAL
   ;

variable
   : VARIABLE
   ;

relop
   : GT
   | LT
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


LITERAL
   : NUMBER
   ;


fragment NUMBER
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


GT
   : '>'
   ;


LT
   : '<'
   ;


EQ
   : '='
   ;


POINT
   : '.'
   ;


POW
   : '^'
   ;


NEWLINE
   : '\n'
   | '\r\n'
   ;


WS
   : [ \t] + -> skip
   ;
