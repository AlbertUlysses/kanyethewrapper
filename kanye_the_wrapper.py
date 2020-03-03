#!/usr/bin/env python3

import urllib.request 
import json


class Kanye():

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


