import unittest
import sys

from basis import interpret

class Variable(unittest.TestCase):
    def test_static(self):
        self.assertEqual(interpret("tests/files/variables/static.code"), ["3.5", "1.5"])

    def test_dynamic(self):
        self.assertEqual(interpret("tests/files/variables/dynamic.code"), ["1.0", "1.5"])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(module=sys.modules[__name__])
    unittest.TextTestRunner(verbosity=2).run(suite)
