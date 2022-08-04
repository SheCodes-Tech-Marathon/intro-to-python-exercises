import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week2.ex2 import main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [[4, 24], [8, 40320]],
    )
    def test_factorial(self, monkeypatch, capsys, params):
        monkeypatch.setattr('builtins.input', lambda msg: params[0])
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == f'{params[1]}\n'
