class Int:
    def __init__(self, n):
        self.val = int(n)

    def negate(self):
        return Int(-self.val)

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


class Float:
    def __init__(self, n):
        self.val = float(n)

    def negate(self):
        return Float(-self.val)

    def mul(self, right):
        return right.mul_float(self)

    def mul_int(self, left):
        return Float(left.val * self.val)

    def mul_float(self, left):
        return Float(left.val * self.val)

    def div(self, right):
        return right.div_float(left)

    def div_int(self, left):
        return Float(left.val / self.val)

    def div_float(self, left):
        return Float(left.val / self.val)
