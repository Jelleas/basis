import sys

from basis import interpret

def test_fib_it():
    assert interpret("examples/fib_it.code") == ["8"]

def test_fib_rec_double():
    assert interpret("examples/fib_rec_double.code") == ["8"]

def test_fib_rec_tail():
    assert interpret("examples/fib_rec_tail.code") == ["8"]

def test_greedy():
    assert interpret("examples/greedy.code") == ["4"]
