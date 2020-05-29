import pytest


def test_west():
    pass

def test_bound_2():
    pass

def test_watch_the_throne():
    pass

def test_heard_em_say():
    from kanye_the_wrapper.kanye_the_wrapper import Kanye
    test_variable = Kanye()
    with pytest.raises(KeyError) as exception_info:
        test_variable.heard_em_say()
    assert exception_info.match('The dictionary is empty.')
