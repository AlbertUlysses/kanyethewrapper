import requests


class Kanye():

    """
    """

    def west(self) -> str:
        r = requests.get('https://api.kanye.rest')
        json_call = r.json()
        diction = dict(json_call)
        payload = str(diction['quote'])
        return payload 



