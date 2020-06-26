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


