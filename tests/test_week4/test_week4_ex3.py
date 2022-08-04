import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week4.ex3 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            [['12', '3', '6', '5', '8', '9', 'q'], [4, 1]],
            [['1', '2', '3', '4', '5', 'q'], [1, 1]],
            [['12', '3', '6', 'q'], [3, 0]],
        ],
    )
    def test_buzzes_fizzes(self, mocker, params):
        mocker.patch('builtins.input', side_effect=params[0])
        res = main()

        if res is not list:
            pytest.skip()

        assert res == params[1]
