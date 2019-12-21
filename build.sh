java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener basis/grammar/Basis.g4
mv "basis/grammar/BasisParser.py" "basis/lang/"
mv "basis/grammar/BasisLexer.py" "basis/lang/"
mv "basis/grammar/BasisVisitor.py" "basis/lang/"
