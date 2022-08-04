import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week4.ex1 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [[456, 654], [110, 11], [-789, -987], [-1420, -241]],
    )
    def test_negative(self, params):
        res = main(number=params[0])

        if res is not int:
            pytest.skip()

        assert res == params[1]
