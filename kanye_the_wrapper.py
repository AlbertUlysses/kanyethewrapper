#!/usr/bin/env python3 
import urllib.request 
import json


class Kanye():

    def __init__(self):
        self.saved_quotes = {} 
        self.quote_counter = 0
        self.last_quote = None
        self.saved = 5

    def watch_the_throne(self) -> str:
        """Saves the last quote."""
        if self.last_quote:
            if self.quote_counter >= self.saved:
                self.quote_counter = 0
            self.saved_quotes[self.quote_counter + 1] = self.last_quote
            self.quote_counter += 1
            return 'Quote Saved'
        raise Exception('No quotes to save, try to call the API first.')

    def west(self) -> str:
        """Returns a Kanye West quote."""
        location = 'https://api.kanye.rest'
        req_call = urllib.request.Request(location, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req_call)
        read_content = content.read()
        payload = json.loads(read_content.decode("utf-8"))
        convert_json = dict(payload)
        self.last_quote = str(convert_json['quote'])
        return self.last_quote

    def heard_em_say(self):
        """Returns a list of saved qoutes."""
        if self.saved_quotes:
            return self.saved_quotes 
        else:
            return "I can't tell you nothin'"
