#!/usr/bin/env python3

import urllib.request 
import json


class Kanye():

    def __init__(self):
        self.saved_quotes = {}


    def west(self) -> str:
        """Returns a Kanye West quote."""
        location = 'https://api.kanye.rest'
        req_call = urllib.request.Request(location, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req_call)
        read_content = content.read()
        payload = json.loads(read_content.decode("utf-8"))
        convert_json = dict(payload)
        str_quote = str(convert_json['quote'])
        return str_quote 


    def heard_em_say(self, diction=None) -> dict:
        """Returns a dictionary of saved qoutes."""
        if diction:
            return "Filler text"
        else:
            return "I can't tell you nothin'"
