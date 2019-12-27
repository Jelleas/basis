class Evaluable:
    def eval(self):
        raise NotImplementedError()

class Assignable(Evaluable):
    def assign(self, val):
        raise NotImplementedError()
