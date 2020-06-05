import pytest
from kanyethewrapper.kanyethewrapper import Kanye


@pytest.fixture
def example_var():
    test_var = Kanye()
    yield test_var 
    test_var.saved_quotes = {}


class TestWest(object):
    def test_west(self):
        pass


class TestBound2(object):

    def test_bound_2_larger_int(self, example_var):
        """Tests that the dictionary can grow larger."""
        actual = example_var.bound_2(10)
        expected = 'The dictionary can save 10 quotes.'
        assert actual == expected

    def test_bound_2_smaller_int(self, example_var):
        """Tests that the dictionary can shrink."""
        actual = example_var.bound_2(5)
        expected = 'The dictionary can save 5 quotes.'
        assert actual == expected
        for _ in range(5):
            example_var.west()
            example_var.watch_the_throne()
        first_item = example_var.saved_quotes[1]
        third_item = example_var.saved_quotes[3]
        example_var.bound_2(3)
        assert first_item == example_var.saved_quotes[1]
        assert third_item == example_var.saved_quotes[3]
        with pytest.raises(KeyError):
            example_var.saved_quotes[4]

    def test_bound_2_bad_args(self, example_var):
        """Tests that bound_2 needs an int"""
        with pytest.raises(TypeError):
            example_var.bound_2()


class TestWatchTheThrone(object):

    def test_watch_the_throne(self):
        pass


class TestHeardEmSay(object):

    def test_heard_em_say(self, example_var):
        """Tests that without calling west() this method returns an error"""
        with pytest.raises(KeyError) as exception_info:
            example_var.heard_em_say()
        assert exception_info.match('The dictionary is empty.')
