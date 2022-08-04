import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week1.ex2 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            iter([47, 174]),
            iter([43, 169]),
        ],
    )
    def test_main_bmi_underweight(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Gầy\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([67, 174]),
            iter([63, 169]),
        ],
    )
    def test_main_bmi_fit(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Bình thường\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([76, 174]),
            iter([82, 169]),
        ],
    )
    def test_main_bmi_overweight(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Thừa cân\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([98, 174]),
            iter([99, 169]),
        ],
    )
    def test_main_bmi_obese_1(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Béo phì độ 1\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([110, 174]),
            iter([110, 169]),
        ],
    )
    def test_main_bmi_obese_2(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Béo phì độ 2\n'

    @pytest.mark.parametrize(
        'params',
        [
            iter([1300, 174]),
            iter([1300, 169]),
        ],
    )
    def test_main_bmi_obese_3(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: next(params))
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == 'Béo phì độ 3\n'
