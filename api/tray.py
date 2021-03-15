from api.consulta import Consulta

class Tray:
    def __init__(self):
        self._url_api    = 'https://api.fbits.net/'
        self._key        = ''
        self._headers    = {'Authorization':'BASIC '+str(self._key)}
        self._consulta   = Consulta(self._url_api)
        self._json_final = {}