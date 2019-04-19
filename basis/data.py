import logger

class Int:
    def __init__(self, n):
        self.val = int(n)

    def negate(self):
        return Int(-self.val)

    def add(self, right):
        return right.add_int(self)

    def add_int(self, left):
        return Int(left.val + self.val)

    def add_float(self, left):
        return Float(self.val).add_float(left)

    def sub(self, right):
        return right.sub_int(self)

    def sub_int(self, left):
        return Int(left.val - self.val)

    def sub_float(self, left):
        return Float(self.val).sub_float(left)

    def mul(self, right):
        return right.mul_int(self)

    def mul_int(self, left):
        return Int(left.val * self.val)

    def mul_float(self, left):
        return Float(self.val).mul_float(left)

    def div(self, right):
        return right.div_int(self)

    def div_int(self, left):
        return Int(left.val // self.val)

    def div_float(self, left):
        return Float(self.val).div_float(left)

    def __str__(self):
        return f"I{self.val}"

class Float:
    def __init__(self, n):
        self.val = float(n)

    def negate(self):
        return Float(-self.val)

    def add(self, right):
        return right.add_float(self)

    def add_int(self, left):
        return self.add_float(Float(left.val))

    def add_float(self, left):
        return Float(left.val + self.val)

    def sub(self, right):
        return right.sub_float(self)

    def sub_int(self, left):
        return self.sub_float(Float(left.val))

    def sub_float(self, left):
        return Float(left.val - self.val)

    def mul(self, right):
        return right.mul_float(self)

    def mul_int(self, left):
        with logger.context("CONV FLOAT") as log:
            left_float = Float(left.val)
            log(f"{left} * {self} => {left_float} * {self}")
            return self.mul_float(left_float)

    def mul_float(self, left):
        with logger.context("MUL FLOAT") as log:
            res = Float(left.val * self.val)
            log(f"{left} * {self} => {logger.emphasize(res)}")
            return res

    def div(self, right):
        return right.div_float(self)

    def div_int(self, left):
        with logger.context("CONV FLOAT") as log:
            left_float = Float(left.val)
            log(f"{left} / {self} => {left_float} / {self}")
            return self.div_float(left_float)

    def div_float(self, left):
        with logger.context("DIV FLOAT") as log:
            res = Float(left.val / self.val)
            log(f"{left} / {self} => {logger.emphasize(res)}")
            return res

    def __str__(self):
        return f"F{self.val}"
