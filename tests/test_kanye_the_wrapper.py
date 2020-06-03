import pytest
from kanye_the_wrapper.kanye_the_wrapper import Kanye


def test_west():
    pass


def test_bound_2():
    test_variable1 = Kanye()
    actual = test_variable1.bound_2(10)
    expected = 'The dictionary can save 10 quotes.'
    assert actual == expected
    test_variable2 = Kanye()
    actual = test_variable2.bound_2(12)
    expected = 'The dictionary can save 12 quotes.'
    assert actual == expected
    actual = test_variable1.bound_2(5)
    expected = 'The dictionary can save 5 quotes.'
    assert actual == expected
    for _ in range(5):
        test_variable1.west()
        test_variable1.watch_the_throne()
    first_item = test_variable1.saved_quotes[1]
    third_item = test_variable1.saved_quotes[3]
    test_variable1.bound_2(3)
    assert first_item == test_variable1.saved_quotes[1]
    assert third_item == test_variable1.saved_quotes[3]
    with pytest.raises(KeyError):
        test_variable1.saved_quotes[5]
    test_variable3 = Kanye()
    with pytest.raises(TypeError):
        test_variable3.bound_2()
    

def test_watch_the_throne():
    pass


def test_heard_em_say():
    test_class = Kanye()
    with pytest.raises(KeyError) as exception_info:
        test_class.heard_em_say()
    assert exception_info.match('The dictionary is empty.')
