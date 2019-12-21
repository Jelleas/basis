import unittest

from basis import interpret

class Example(unittest.TestCase):
    def test_fib_it(self):
        self.assertEqual(interpret("examples/fib_it.basis")[0], "8")

    def test_fib_rec_double(self):
        self.assertEqual(interpret("examples/fib_rec_double.basis")[0], "8")

    def test_fib_rec_tail(self):
        self.assertEqual(interpret("examples/fib_rec_tail.basis")[0], "8")

    def test_greedy(self):
        self.assertEqual(interpret("examples/greedy.basis")[0], "4")
