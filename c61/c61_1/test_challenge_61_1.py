from pprint import pprint
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from test_cases_ch_61_1 import test_inp, test_out


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


@mock.patch('builtins.input', side_effect=[str(len(test_out))] + test_inp)
def test_challenge_61_1(input: Callable) -> None:
    
    with Capturing() as output:
        start = perf_counter()
    
        import challenge_61_1  # change name to your file with solution name without extension
        
        end = perf_counter()
    
    passed = i = ii = 0
    for i in range(1, len(test_out) + 1):
        map_rows = int(test_inp[ii + 1].split()[0]) + 4
        inp = test_inp[ii: ii + map_rows]
        out, exp = output[i - 1], test_out[i - 1]
        ii += map_rows
        if out != exp:
            print(f'Test nr:{i}\n    inp:')
            print(*inp, sep="\n")
            print('Your output:')
            pprint(out)
            print('Expected:')
            pprint(exp)
        else:
            passed += 1

    print(f"Passed: {passed}/{i} tests")
    print(f"Finished in: {end - start} seconds")


if __name__ == "__main__":
    test_challenge_61_1()
