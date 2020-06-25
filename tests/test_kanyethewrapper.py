import pytest
import kanyethewrapper as kw


@pytest.fixture
def example_var():
    test_var = kw.Kanye()
    yield test_var 
    test_var.saved_quotes = {}


class TestWest(object):

    def test_west(self, example_var):
        """Tests that we are getting a string and that we can access it"""
        example_var.west()
        assert example_var.last_quote is not None

        first_quote = example_var.last_quote
        example_var.west()
        assert first_quote != example_var.last_quote


class TestBound2(object):

    def test_bound_2_larger_int(self, example_var):
        """Tests that the dictionary can grow larger."""
        actual = example_var.bound_2(10)
        expected = 'The dictionary can save 10 quotes.'
        assert actual == expected
        assert example_var.saved == 10

    def test_bound_2_smaller_int(self, example_var):
        """Tests that the dictionary can shrink."""
        actual = example_var.bound_2(5)
        expected = 'The dictionary can save 5 quotes.'
        assert actual == expected
        assert example_var.saved == 5

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


