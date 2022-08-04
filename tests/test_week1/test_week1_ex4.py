import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week1.ex4 import main, main_advance


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            [12345, 5],
            [200, 0],
        ],
    )
    def test_main(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params[0])
        main()
        out, err = capsys.readouterr()

        if out is not int:
            pytest.skip()

        assert out == f'{params[1]}\n'

    @pytest.mark.parametrize(
        'params',
        [
            [69, 'Fizz\n'],
            [2015, 'FizzBuzz\n'],
            [35, 'Buzz\n'],
            [134, ''],
        ],
    )
    def test_main_advance(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params[0])
        main_advance()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        if out == '':
            assert True
        else:
            assert out == params[1]
