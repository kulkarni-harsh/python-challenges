from pprint import pprint
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from test_cases_ch_65 import test_inp, test_out


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


@mock.patch("builtins.input", side_effect=[str(len(test_out))] + test_inp)
def test_challenge_65(input: Callable) -> None:
    red, green, yellow, cyan, reset = (
        "\u001b[31m",
        "\u001b[32m",
        "\u001b[33m",
        "\u001b[36m",
        "\u001b[0m",
    )

    with Capturing() as output:
        start = perf_counter()

        import challenge_65  #  challenge_63_1  # change name to your file with solution name without extension

        end = perf_counter()

    passed = i = 0
    for i in range(1, len(test_out) + 1):
        out, exp, inp = output[i - 1], test_out[i - 1], test_inp[i - 1]
        if out != exp:
            print(f"Test nr:{i}\n      Input: {cyan}{inp}{reset}")
            print(f"Your output: {red}{out}{reset}")
            print(f"   Expected: {green}{exp}{reset}")
        else:
            passed += 1

    print(f"\nPassed: {green if passed == i else red}{passed}/{i}{reset} tests")
    print(f"Finished in: {yellow}{end - start:.4f}{reset} seconds")


if __name__ == "__main__":
    test_challenge_65()
