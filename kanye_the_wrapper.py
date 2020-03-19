#!/usr/bin/env python3 
import urllib.request 
import json


class Kanye():

    def __init__(self, saved=5):
        self.saved_quotes = [] 
        self.saved = saved
        self.quote_counter = 0
        self.last_quote = None

    def watch_the_throne(self):
        """Saves the last quote."""
        if self.last_quote:
            self.saved_quotes.append(self.last_quote)
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

    def heard_em_say(self) -> list:
        """Returns a list of saved qoutes."""
        if self.saved_quotes:
            return self.saved_quotes 
        else:
            return "I can't tell you nothin'"
