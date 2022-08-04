import os
import sys

import pytest

sys.path.append(f'{os.getcwd()}\\code')
import week4.ex2 as main


class TestMain:
    @pytest.mark.parametrize(
        'params',
        [
            ['David', 23, ['read', 'write']],
            ['Alex', 32, ['football', 'basketball']],
            ['Emilia', 30, ['pool']],
            ['Andy', 13, ['fishing', 'catch']],
        ],
    )
    def test_class_object(self, params):
        if not hasattr(main, 'Person'):
            pytest.skip()

        person = main.Person(name=params[0], age=params[1], hobbies=params[2])

        assert type(person.name) == str
        assert type(person.age) == int
        assert type(person.hobbies) == list
