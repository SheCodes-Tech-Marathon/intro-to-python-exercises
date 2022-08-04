import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week3.ex2 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [['some string', 11], [['Pizza', 'Pasta', 'Pancake'], 3]],
    )
    def test_len(self, params):
        res = main(iterable=params[0])

        if res is not str or res == '':
            pytest.skip()

        assert res == params[1]
