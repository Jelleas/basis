import unittest
import sys

from basis import interpret

class Condition(unittest.TestCase):
    def test_if_true(self):
        self.assertEqual(interpret("tests/files/conditions/if_true.code"), ["11"])

    def test_if_false(self):
        self.assertEqual(interpret("tests/files/conditions/if_false.code"), ["0"])

    def test_if_or(self):
        self.assertEqual(interpret("tests/files/conditions/if_or.code"), ["-3"])

    def test_if_and(self):
        self.assertEqual(interpret("tests/files/conditions/if_and.code"), ["5"])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(module=sys.modules[__name__])
    unittest.TextTestRunner(verbosity=2).run(suite)
