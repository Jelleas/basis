java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener basis/antlr/Basis.g4
mv "basis/antlr/BasisParser.py" "basis/lang/"
mv "basis/antlr/BasisLexer.py" "basis/lang/"
mv "basis/antlr/BasisVisitor.py" "basis/lang/"
