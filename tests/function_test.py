import sys

from basis import interpret

def test_single_arg():
    assert interpret("tests/files/function/single_arg.code") == ["3"]
