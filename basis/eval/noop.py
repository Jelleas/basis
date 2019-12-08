from . import Evaluable
from . import Null

class NoOp(Evaluable):
    def eval(self):
        return Null()

    def __str__(self):
        return ""
