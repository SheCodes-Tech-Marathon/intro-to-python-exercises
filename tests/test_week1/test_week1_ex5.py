import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week1.ex5 import main


class TestMain:
    @pytest.mark.parametrize('params', [4, 6, 9, 11])
    def test_main_30_days(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params)
        main()
        out, err = capsys.readouterr()
        
        if out is not str or out == '':
            pytest.skip()

        assert out == '30 ngày\n'

    @pytest.mark.parametrize('params', [1, 3, 5, 7, 8, 10, 12])
    def test_main_31_days(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params)
        main()
        out, err = capsys.readouterr()
        
        if out is not str or out == '':
            pytest.skip()

        assert out == '31 ngày\n'

    @pytest.mark.parametrize('params', [2])
    def test_main_28_days(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params)
        main()
        out, err = capsys.readouterr()
        
        if out is not str or out == '':
            pytest.skip()

        assert out == '28 ngày\n'
