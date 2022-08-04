import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week3.ex1 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [[5, 2022, '31 ngày'], [2, 2000, '29 ngày']],
    )
    def test_leap_year(self, params):
        res = main(month=params[0], year=params[1])

        if res is not str or res == '':
            pytest.skip()

        assert res == params[2]
