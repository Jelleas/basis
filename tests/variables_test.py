import sys

from basis import interpret

def test_static():
    assert interpret("tests/files/variables/static.code") == ["3.5", "1.5"]

def test_dynamic():
    assert interpret("tests/files/variables/dynamic.code") == ["1.0", "1.5"]
