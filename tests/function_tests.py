import unittest
import sys

from basis import interpret

class Function(unittest.TestCase):
    def test_single_arg(self):
        self.assertEqual(interpret("tests/files/function/single_arg.basis")[0], "3")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(module=sys.modules[__name__])
    unittest.TextTestRunner(verbosity=2).run(suite)
