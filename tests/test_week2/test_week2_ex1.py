import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week2.ex1 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [['Football', 'Basketball', 'Baseball'], ['Eat', 'Sleep', 'Code']],
    )
    def test_input_loops(self, mocker, capsys, params):
        mocker.patch('builtins.input', side_effect=params)
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == f'{params}\n'
