import pytest
import kanyethewrapper as kw

@pytest.fixture
def example_var():
    test_var = kw.Kanye()
    yield test_var
    test_var.saved_quotes = {}

class TestWatchTheThrone(object):
    def test_watch_the_throne(self, example_var):
        """Tests that watch_the_throne is saiving the last quote"""
        example_var.west()
        example_dict = kw.Facts()
        example_dict.watch_the_throne(example_var)
        assert example_dict.saved_quotes[1] == example_var.last_quote

