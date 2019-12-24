from basis import interpret

import pytest
import os
import re

def create(tests):
    def test_func(test_file):
        with open(test_file) as f:
            solution = re.findall(r"//(.*)", f.read())
        assert interpret(test_file) == solution

    return pytest.mark.parametrize("test_file", tests)(test_func)


for root, dirs, files in os.walk("tests/files"):
    tests = [os.path.join(root, f) for f in files if f.endswith(".code")]

    if tests:
        test_name = "test_" + os.path.basename(root)
        globals()[test_name] = create(tests)
