from .kanyethewrapper import Kanye

class Facts():

    def __init__(self):
        self.saved_quotes = {} 
        self.quote_counter = 0
        self.saved = 5
    
    def watch_the_throne(self, kanye_object) -> str:
        """Saves the last quote."""
        if kanye_object.last_quote:
            if self.quote_counter >= self.saved:
                self.quote_counter = 0
            self.saved_quotes[self.quote_counter + 1] = kanye_object.last_quote
            self.quote_counter += 1
            return 'Quote Saved'
        raise Exception('Try calling the API first.')
