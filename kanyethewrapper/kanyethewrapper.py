#!/usr/bin/env python3 
import urllib.request 
import json


class Kanye():

    def __init__(self):
        self.saved_quotes = {} 
        self.quote_counter = 0
        self.last_quote = None
        self.saved = 5

    def bound_2(self, new_saved: int) -> str:
        """Resets the dictionary size for quotes, 
        drops the quotes that are over the new limit."""
        if len(self.saved_quotes) > new_saved: 
            old_dictionary = self.saved_quotes
            self.saved_quotes = {key: value for key,
                    value in old_dictionary.items() if key <= new_saved}
        self.saved = new_saved
        return f'The dictionary can save {self.saved} quotes.' 

    def west(self) -> str:
        """Returns a Kanye West quote."""
        location = 'https://api.kanye.rest'
        req_call = urllib.request.Request(location, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req_call)
        read_content = content.read()
        payload = json.loads(read_content.decode("utf-8"))
        payload_dict = dict(payload)
        self.last_quote = str(payload_dict['quote'])
        return self.last_quote

    def heard_em_say(self) -> dict:
        """Returns a dictionary of saved quotes."""
        if self.saved_quotes:
            return self.saved_quotes 
        raise KeyError('The dictionary is empty.')
