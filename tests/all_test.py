import sys
import helper
import basis.eval.factories.all

helper.tests_from_files(sys.modules[__name__], "tests/files/all", basis.eval.factories.all)
