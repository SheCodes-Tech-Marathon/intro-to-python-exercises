import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
from week5.ex import StringUtilities


class TestMain:
    string_utils = StringUtilities()

    @pytest.mark.parametrize(
        'params',
        [
            ['Adam and Eve', 'Eve and Adam'],
            ['A clear blue sky', 'sky blue clear A'],
            ['Lady', 'Lady'],
            ['A lonely night', 'night lonely A'],
        ],
    )
    def test_reverse_sentence(self, params):
        res = self.string_utils.reverse_sentence(sentence=params[0])

        if res is not str:
            pytest.skip()

        assert res == params[1]

    @pytest.mark.parametrize(
        'params',
        [
            ['I like ice cream', 5],
            ['in the nick of time', 4],
            ['', 0],
            ['I like donut', 5],
        ],
    )
    def test_longest_word_length(self, params):
        res = self.string_utils.longest_word_length(sentence=params[0])

        if res is not int:
            pytest.skip()

        assert res == params[1]

    @pytest.mark.parametrize(
        'params',
        [['{()}[]', True], ['{(', False], ['[(])', False]],
    )
    def test_is_valid_parentheses(self, params):
        res = self.string_utils.is_valid_parentheses(string=params[0])

        if res is not bool:
            pytest.skip()

        assert res == params[1]

    @pytest.mark.parametrize(
        'params',
        [
            ['A very lovely day', 'Averylovelyday'],
            ['So      much           space', 'Somuchspace'],
        ],
    )
    def test_remove_white_spaces(self, params):
        res = self.string_utils.remove_white_spaces(string=params[0])

        if res is not str:
            pytest.skip()

        assert res == params[1]

    @pytest.mark.parametrize(
        'params',
        [['old mcdonald had a farm', 'aaaacddddfhllmmnoor']],
    )
    def test_sort_string(self, params):
        res = self.string_utils.sort_string(string=params[0])

        if res is not str:
            pytest.skip()

        assert res == params[1]
