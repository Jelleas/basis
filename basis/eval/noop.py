from . import Evaluable

class NoOp(Evaluable):
    def eval(self):
        pass

    def __str__(self):
        return ""
