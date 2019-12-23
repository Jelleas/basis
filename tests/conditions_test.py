from basis import interpret

def test_if_true():
    assert interpret("tests/files/conditions/if_true.code") == ["11"]

def test_if_false():
    assert interpret("tests/files/conditions/if_false.code") == ["0"]

def test_if_or():
    assert interpret("tests/files/conditions/if_or.code") == ["-3"]

def test_if_and():
    assert interpret("tests/files/conditions/if_and.code") == ["5"]
