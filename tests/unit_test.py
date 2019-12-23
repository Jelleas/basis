from basis import interpret

import pytest
import os

def create(tests):
    def test_func(test_file, solution_file):
        with open(solution_file) as f:
            solution = [line.strip() for line in f]
        assert interpret(test_file) == solution

    return pytest.mark.parametrize("test_file,solution_file", tests)(test_func)


for root, dirs, files in os.walk("tests/files"):
    tests = []
    for f in files:
        if f.endswith(".code"):
            test_file = os.path.join(root, f)
            solution_file = test_file.replace(".code", ".sol")
            tests.append((test_file, solution_file))

    if tests:
        test_name = "test_" + os.path.basename(root)
        globals()[test_name] = create(tests)
