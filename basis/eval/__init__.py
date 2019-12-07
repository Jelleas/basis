class Evaluable:
    def eval(self):
        raise NotImplementedError()

from .literals import *
from .control import *
from .expressions import *
from .scope import *
from .noop import *
