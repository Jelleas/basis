from basis import interpret
import pytest
import os
import re

def tests_from_files(module, path, factory):
    def create(tests):
        def test_func(test_file):
            with open(test_file) as f:
                solution = re.findall(r"//(.*)", f.read())
            assert interpret(test_file, factory) == solution

        return pytest.mark.parametrize("test_file", tests)(test_func)


    for root, dirs, files in os.walk(path):
        tests = [os.path.join(root, f) for f in files if f.endswith(".code")]

        if tests:
            test_name = "test_" + os.path.basename(root)
            setattr(module, test_name, create(tests))
