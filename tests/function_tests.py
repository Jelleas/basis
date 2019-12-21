import unittest

from basis import interpret

class Function(unittest.TestCase):
    def test_single_arg(self):
        self.assertEqual(interpret("tests/files/function/single_arg.basis")[0], "3")
