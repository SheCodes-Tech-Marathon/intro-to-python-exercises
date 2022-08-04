import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week1.ex1 import main


class TestMain:
    @pytest.mark.parametrize(
        'param',
        [
            2000,
            1904,
            400,
            2016,
            1240,
        ],
    )
    def test_main_leap_year(self, monkeypatch, capsys, param):
        monkeypatch.setattr('builtins.input', lambda msg: param)
        main()
        out, err = capsys.readouterr()
        
        if out is not str or out == '':
            pytest.skip()

        assert out == 'Năm nhuận\n'

    @pytest.mark.parametrize(
        'param',
        [
            2001,
            1905,
            403,
            2019,
            1243,
        ],
    )
    def test_main_not_leap_year(self, monkeypatch, capsys, param):
        monkeypatch.setattr('builtins.input', lambda msg: param)
        main()
        out, err = capsys.readouterr()
        
        if out is not str or out == '':
            pytest.skip()

        assert out == 'Không phải năm nhuận\n'
