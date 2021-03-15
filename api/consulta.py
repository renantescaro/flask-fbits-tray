import requests

class Consulta:
    def __init__(self, url):
        self._url = url


    def get(self, parametros={}, headers={}, endpoint=''):
        return requests.get(url=str(self._url) + str(endpoint), params=parametros, headers=headers)