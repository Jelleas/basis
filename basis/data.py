import basis.logger as logger


__all__ = ["Null", "Int", "Float", "Bool", "String"]


class UnsupportedOperationError(Exception):
    pass


class Null:
    def __eq__(self, other):
        return Bool(str(isinstance(other, Null)))

    def __str__(self):
        return "null"


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
            log(f"{left} + {self} => {left} + {logger.emphasize(self_float)}")
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
            log(f"{left} - {self} => {left} - {logger.emphasize(self_float)}")
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
            log(f"{left} * {self} => {left} * {logger.emphasize(self_float)}")
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
            log(f"{left} / {self} => {left} / {logger.emphasize(self_float)}")
        return self_float.div_float(left)

    def mod(self, right):
        return right.mod_int(self)

    def mod_int(self, left):
        with logger.context("MOD INT") as log:
            res = Int(left.val % self.val)
            log(f"{left} % {self} => {logger.emphasize(res)}")
            return res

    def mod_float(self, left):
        with logger.context("CONV FLOAT") as log:
            self_float = Float(self.val)
            log(f"{left} % {self} => {left} % {logger.emphasize(self_float)}")
        return self_float.mod_float(left)

    def eq(self, other):
        return _compare(self, other, (Int, Float), "EQ INT", "==", lambda: self.val == other.val)

    def neq(self, other):
        return _compare(self, other, (Int, Float), "NEQ INT", "!=", lambda: self.val != other.val)

    def lt(self, other):
        return _compare(self, other, (Int, Float), "LT INT", "<", lambda: self.val < other.val)

    def gt(self, other):
        return _compare(self, other, (Int, Float), "GT INT", ">", lambda: self.val > other.val)

    def let(self, other):
        return _compare(self, other, (Int, Float), "LET INT", "<=", lambda: self.val <= other.val)

    def get(self, other):
        return _compare(self, other, (Int, Float), "GET INT", ">=", lambda: self.val >= other.val)

    def __str__(self):
        return f"{self.val}"


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
            log(f"{left} + {self} => {logger.emphasize(left_float)} + {self}")
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
            log(f"{left} - {self} => {logger.emphasize(left_float)} - {self}")
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
            log(f"{left} * {self} => {logger.emphasize(left_float)} * {self}")
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
            log(f"{left} / {self} => {logger.emphasize(left_float)} / {self}")
        return self.div_float(left_float)

    def div_float(self, left):
        with logger.context("DIV FLOAT") as log:
            res = Float(left.val / self.val)
            log(f"{left} / {self} => {logger.emphasize(res)}")
            return res

    def mod(self, right):
        return right.mod_float(self)

    def mod_int(self, left):
        with logger.context("CONV FLOAT") as log:
            left_float = Float(left.val)
            log(f"{left} % {self} => {logger.emphasize(left_float)} % {self}")
        return self.mod_float(left_float)

    def mod_float(self, left):
        with logger.context("MOD FLOAT") as log:
            res = Float(left.val % self.val)
            log(f"{left} % {self} => {logger.emphasize(res)}")
            return res

    def eq(self, other):
        return _compare(self, other, (Int, Float), "EQ FLOAT", "==", lambda: self.val == other.val)

    def neq(self, other):
        return _compare(self, other, (Int, Float), "NEQ FLOAT", "!=", lambda: self.val != other.val)

    def lt(self, other):
        return _compare(self, other, (Int, Float), "LT FLOAT", "<", lambda: self.val < other.val)

    def gt(self, other):
        return _compare(self, other, (Int, Float), "GT FLOAT", ">", lambda: self.val > other.val)

    def let(self, other):
        return _compare(self, other, (Int, Float), "LET FLOAT", "<=", lambda: self.val <= other.val)

    def get(self, other):
        return _compare(self, other, (Int, Float), "GET FLOAT", ">=", lambda: self.val >= other.val)

    def __str__(self):
        return f"{self.val}"


class Bool:
    def __init__(self, b):
        b_lower = b.lower()

        if b_lower != "false" and b_lower != "true":
            raise ValueError(f"booleans can only be true or false, not {b}")

        self.val = b_lower == "true"

    def eq(self, other):
        with logger.context("EQ BOOL") as log:
            if not isinstance(other, Bool):
                raise UnsupportedOperationError(f"Cannot compare (==) {self} and {other}")

            result = Bool(str(self.val == other.val))
            log(f"{self} == {other} => {logger.emphasize(result)}")
            return result

    def neq(self, other):
        with logger.context("NEQ BOOL") as log:
            if not isinstance(other, Bool):
                raise UnsupportedOperationError(f"Cannot compare (!=) {self} and {other}")

            result = Bool(str(self.val != other.val))
            log(f"{self} != {other} => {logger.emphasize(result)}")
            return result

    def not_(self):
        with logger.context("NOT BOOL") as log:
            result = Bool(str(not self.val))
            log(f"!{self} => {logger.emphasize(result)}")
            return result

    def or_(self, other):
        with logger.context("OR BOOL") as log:
            if not isinstance(other, Bool):
                raise UnsupportedOperationError(f"Cannot compare (||) {self} and {other}")

            result = Bool(str(other.val or self.val))
            log(f"{self} || {other} => {logger.emphasize(result)}")
            return result

    def and_(self, other):
        with logger.context("AND BOOL") as log:
            if not isinstance(other, Bool):
                raise UnsupportedOperationError(f"Cannot compare (&&) {self} and {other}")

            result = Bool(str(other.val and self.val))
            log(f"{self} && {other} => {logger.emphasize(result)}")
            return result

    def __str__(self):
        return f"{self.val}"


class String:
    def __init__(self, text):
        self.text = str(text)

    def index(self, index):
        if not isinstance(index, Int):
            raise UnsupportedOperationError(f"Cannot index into String with index {index}")

        return String(self.text[index.val])

    def index_assign(self, index, val):
        if not isinstance(index, Int):
            raise UnsupportedOperationError(f"Cannot index into String with index {index}")

        if not isinstance(val, String):
            raise UnsupportedOperationError(f"Cannot assign value {val} to an index of String")

        i = index.val
        self.text = self.text[:i] + val.text + self.text[i + 1:]

    def eq(self, other):
        with logger.context("EQ STRING") as log:
            if not isinstance(other, String):
                raise UnsupportedOperationError(f"Cannot compare (==) {self} and {other}")

            result = Bool(str(self.text == other.text))
            log(f"{self} == {other} => {logger.emphasize(result)}")
            return result

    def __str__(self):
        return f'"{self.text}"'


def _compare(left, right, accepted_types, log_msg, symbol, operation):
    with logger.context(log_msg) as log:
        if not any(isinstance(right, t) for t in accepted_types):
            raise UnsupportedOperationError(f"Cannot compare: {left} {symbol} {right}")

        result = Bool(str(operation()))
        log(f"{left} {symbol} {right} => {logger.emphasize(result)}")
        return result
