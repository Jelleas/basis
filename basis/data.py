import basis.logger as logger


__all__ = ["Int", "Float", "Bool"]


class UnsupportedOperationError(Exception):
    pass


class Int:
    def __init__(self, n):
        self.val = int(n)

    def negate(self):
        return Int(-self.val)

    def add(self, right):
        return right.add_int(self)

    def add_int(self, left):
        with logger.context("ADD INT") as log:
            res = Int(left.val + self.val)
            log(f"{left} + {self} => {logger.emphasize(res)}")
            return res

    def add_float(self, left):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{left} + {self} => {left} + {self_float}")
        return self_float.add_float(left)

    def sub(self, right):
        return right.sub_int(self)

    def sub_int(self, left):
        with logger.context("SUB INT") as log:
            res = Int(left.val - self.val)
            log(f"{left} - {self} => {logger.emphasize(res)}")
            return res

    def sub_float(self, left):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{left} - {self} => {left} - {self_float}")
        return self_float.sub_float(left)

    def mul(self, right):
        return right.mul_int(self)

    def mul_int(self, left):
        with logger.context("MUL INT") as log:
            res = Int(left.val * self.val)
            log(f"{left} * {self} => {logger.emphasize(res)}")
            return res

    def mul_float(self, left):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{left} * {self} => {left} * {self_float}")
        return self_float.mul_float(left)

    def div(self, right):
        return right.div_int(self)

    def div_int(self, left):
        with logger.context("DIV INT") as log:
            res = Int(left.val // self.val)
            log(f"{left} / {self} => {logger.emphasize(res)}")
            return res

    def div_float(self, left):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{left} / {self} => {left} / {self_float}")
        return self_float.div_float(left)

    def eq(self, other):
        return other.eq_int(self)

    def eq_bool(self, other):
        raise UnsupportedOperationError("Cannot compare booleans and floats")

    def eq_int(self, other):
        with logger.context("EQ INT") as log:
            result = Bool(str(other.val == self.val))
            log(f"{other} == {self} => {logger.emphasize(result)}")
            return result

    def eq_float(self, other):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{other} == {self} => {other} == {self_float}")
        return self_float.eq_float(other)

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
        with logger.context("CONV FLOAT") as log:
            left_float = Float(left.val)
            log(f"{left} + {self} => {left_float} + {self}")
        return self.add_float(left_float)

    def add_float(self, left):
        with logger.context("ADD FLOAT") as log:
            res = Float(left.val + self.val)
            log(f"{left} + {self} => {logger.emphasize(res)}")
            return res

    def sub(self, right):
        return right.sub_float(self)

    def sub_int(self, left):
        with logger.context("CONV FLOAT") as log:
            left_float = Float(left.val)
            log(f"{left} - {self} => {left_float} - {self}")
        return self.sub_float(left_float)

    def sub_float(self, left):
        with logger.context("SUB FLOAT") as log:
            res = Float(left.val - self.val)
            log(f"{left} - {self} => {logger.emphasize(res)}")
            return res

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

    def eq(self, other):
        return other.eq_float(self)

    def eq_bool(self, other):
        raise UnsupportedOperationError("Cannot compare booleans and floats")

    def eq_int(self, other):
        with logger.context("CONV FLOAT") as log:
            other_float = Float(other.val)
            log(f"{other} == {self} => {other_float} == {self}")
        return self.eq_float(other)

    def eq_float(self, other):
        with logger.context("EQ FLOAT") as log:
            result = Bool(str(other.val == self.val))
            log(f"{other} == {self} => {logger.emphasize(result)}")
            return result

    def __str__(self):
        return f"F{self.val}"


class Bool:
    def __init__(self, b):
        b_lower = b.lower()

        if b_lower != "false" and b_lower != "true":
            raise ValueError(f"booleans can only be true or false, not {b}")

        self.val = b_lower == "true"

    def eq(self, other):
        return other.eq_bool(self)

    def eq_bool(self, other):
        with logger.context("EQ BOOL") as log:
            result = Bool("true" if self.val == other.val else "false")
            log(f"{self} == {other} => {result}")
            return result

    def eq_int(self, other):
        with logger.context("EQ BOOL") as log:
            result = Bool("false")
            log(f"{self} == {other} => {result}")
            return result

    def eq_float(self, other):
        with logger.context("EQ BOOL") as log:
            result = Bool("false")
            log(f"{self} == {other} => {result}")
            return result

    def __str__(self):
        return f"B{self.val}"
