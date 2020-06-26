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

    def heard_em_say(self) -> dict:
        """Returns a dictionary of saved quotes."""
        if self.saved_quotes:
            return self.saved_quotes 
        raise KeyError('The dictionary is empty.')

    def bound_2(self, new_saved: int) -> str:
        """Resets the dictionary size for quotes, 
        drops the quotes that are over the new limit."""
        if len(self.saved_quotes) > new_saved: 
            old_dictionary = self.saved_quotes
            self.saved_quotes = {key: value for key,
                    value in old_dictionary.items() if key <= new_saved}
        self.saved = new_saved
        return f'The dictionary can save {self.saved} quotes.'
