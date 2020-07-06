#!/usr/bin/env python3 
import urllib.request 
import json


class Kanye():

    def __init__(self) -> None:
        self.last_quote = None

    def west(self) -> str:
        """Returns a Kanye West quote."""
        location = 'https://api.kanye.rest'
        req_call = urllib.request.Request(location, headers={"User-Agent": 
                                                             "Mozilla/5.0"})
        content = urllib.request.urlopen(req_call)
        read_content = content.read()
        payload = json.loads(read_content.decode("utf-8"))
        payload_dict = dict(payload)
        self.last_quote = str(payload_dict['quote'])
        return self.last_quote

