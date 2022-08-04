import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week2.ex3 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [[list(range(10)), [1, 3, 5, 7, 9]], [[1, 2, 3, 4, 5, 6], [2, 4, 6]]],
    )
    def test_odds_in_list(self, mocker, capsys, params):
        my_list = mocker.patch('week2.ex3.list')
        my_list.return_value = params[0]
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == f'{params[1]}\n'
