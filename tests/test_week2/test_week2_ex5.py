import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
sys.path.append(f'{os.getcwd()}\\tests')
from helpers import get_week2_ex5_pattern
from week2.ex5 import main


class TestMain:
    def test_print_pattern(self, capsys):
        pattern = get_week2_ex5_pattern()
        main()
        out, err = capsys.readouterr()

        if out is not str or out == '':
            pytest.skip()

        assert out == pattern
