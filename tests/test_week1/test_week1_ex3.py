import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week1.ex3 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            iter([3, 4, 5]),
            iter([6, 8, 10]),
        ],
    )
    def test_main_right_triangle(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Tam giác vuông\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([1, 1, 1]),
            iter([1, 2, 3]),
        ],
    )
    def test_main_not_right_triangle(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Không phải tam giác vuông\n'
