import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week3.ex3 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            ['POKEMON', 'Viết hoa'],
            ['pikachu', 'Viết thường'],
            ['Bulbasaur', 'Viết hoa và viết thường'],
        ],
    )
    def test_check_case(self, params):
        res = main(word=params[0])

        if res is not str or res == '':
            pytest.skip()

        assert res == params[1]
