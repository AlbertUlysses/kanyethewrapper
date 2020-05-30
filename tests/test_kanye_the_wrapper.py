import pytest
from kanye_the_wrapper.kanye_the_wrapper import Kanye


def test_west():
    pass


def test_bound_2():
    test_class = Kanye()
    actual = test_class.bound_2(10)
    expected = 'The dictionary can save 10 quotes.'
    assert actual == expected
    actual = test_class.bound_2(5)
    expected = 'The dictionary can save 5 quotes.'
    assert actual == expected
    

def test_watch_the_throne():
    pass


def test_heard_em_say():
    test_class = Kanye()
    with pytest.raises(KeyError) as exception_info:
        test_class.heard_em_say()
    assert exception_info.match('The dictionary is empty.')
