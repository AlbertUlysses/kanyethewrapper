#!/usr/bin/env python3

import urllib.request 
import json


class Kanye():

    def __init__(self, saved=5):
        self.saved_quotes = [] 
        self.saved = saved
        self.quote_counter = 0

    def west(self) -> str:
        """Returns a Kanye West quote."""
        location = 'https://api.kanye.rest'
        req_call = urllib.request.Request(location, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req_call)
        read_content = content.read()
        payload = json.loads(read_content.decode("utf-8"))
        convert_json = dict(payload)
        str_quote = str(convert_json['quote'])
        if len(self.saved_quotes) < self.saved: 
            self.saved_quotes.append(str_quote)  
            self.quote_counter += 1
        elif len(self.saved_quotes) == self.saved and \
                self.quote_counter == self.saved:
            self.quote_counter = 0
            self.saved_quotes[self.quote_counter] = str_quote
            self.quote_counter += 1
        else:
            self.saved_quotes[self.quote_counter] = str_quote
            self.quote_counter += 1
        return str_quote

    def heard_em_say(self) -> list:
        """Returns a list of saved qoutes."""
        if self.saved_quotes:
            return self.saved_quotes 
        else:
            return "I can't tell you nothin'"
