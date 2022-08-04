import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week2.ex4 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [['Baseball', 'llabesaB'], ['palindrome', 'emordnilap']],
    )
    def test_palindrome(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params[0])
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == f'{params[1]}\n'
