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

    def test_watch_the_throne_past_limit(self, example_var):
        """Test watch_the_throne limit acts correctly."""        
        example_dict = kw.Facts()
        for _ in range(5):
            example_var.west()
            example_dict.watch_the_throne(example_var)
        old_quote = example_dict.saved_quotes[1]
        second_quote = example_dict.saved_quotes[2]
        example_var.west()
        example_dict.watch_the_throne(example_var)
        assert old_quote != example_dict.saved_quotes[1]
        assert second_quote == example_dict.saved_quotes[2]

    def test_watch_the_throne_error(self, example_var):
        """Tests that without calling west() this method returns an error"""
        example_dict = kw.Facts()
        with pytest.raises(Exception) as exception_info:
            example_dict.watch_the_throne(example_var)
        assert exception_info.match('Try calling the API first.')

class TestHeardEmSay(object):

    def test_heard_em_say_error(self, example_var):
        """Tests that the  wacth_the_throne() is called or else an error is given"""
        example_dict = kw.Facts()
        with pytest.raises(KeyError) as exception_info:
            example_dict.heard_em_say()
        assert exception_info.match('The dictionary is empty.')

    def test_heard_em_say(self, example_var):
        """Tests heard_em_say"""
        example_dict = kw.Facts()
        for _ in range(3):
            example_var.west()
            example_dict.watch_the_throne(example_var)
        assert example_dict.heard_em_say() == example_dict.saved_quotes
        assert len(example_dict.saved_quotes.keys()) == 3
        assert len(example_dict.saved_quotes.values()) == 3

