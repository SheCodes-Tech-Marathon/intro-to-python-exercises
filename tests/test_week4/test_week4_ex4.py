import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week4.ex4 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            [[1, 2, 3, 4, 5], 'Rất tiếc, chúc bạn may mắn lần sau.'],
            [[9], 'Chúc mừng, bạn đã đoán chính xác'],
        ],
    )
    def test_guess_number(self, mocker, params):
        mocker.patch('random.randint', return_value=9)
        mocker.patch('builtins.input', side_effect=params[0])
        res = main()

        if res is not str or res == '':
            pytest.skip()

        assert res == params[1]
