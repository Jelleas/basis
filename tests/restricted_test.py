import sys
import helper
import basis.eval.factories.restricted

helper.tests_from_files(sys.modules[__name__], "tests/files/restricted", basis.eval.factories.restricted)
