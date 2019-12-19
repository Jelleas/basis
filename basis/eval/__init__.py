class Evaluable:
    def eval(self):
        raise NotImplementedError()

class Assignable(Evaluable):
    def assign(self, val):
        raise NotImplementedError()

from .literals import *
from .control import *
from .expressions import *
from .scope import *
from .noop import *
