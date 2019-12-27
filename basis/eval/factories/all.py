from basis.eval.constructs import *
from basis.eval.stdlib import *
from basis.eval.types import *

def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])
