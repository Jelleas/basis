import unittest
import sys

from basis import interpret

class Example(unittest.TestCase):
    def test_fib_it(self):
        self.assertEqual(interpret("examples/fib_it.code")[0], "8")

    def test_fib_rec_double(self):
        self.assertEqual(interpret("examples/fib_rec_double.code")[0], "8")

    def test_fib_rec_tail(self):
        self.assertEqual(interpret("examples/fib_rec_tail.code")[0], "8")

    def test_greedy(self):
        self.assertEqual(interpret("examples/greedy.code")[0], "4")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(module=sys.modules[__name__])
    unittest.TextTestRunner(verbosity=2).run(suite)
