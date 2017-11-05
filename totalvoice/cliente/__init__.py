# coding=utf-8
from totalvoice.helper import utils

class Cliente(object):
      
    access_token = None
    host = None
    _api = None
    _chamada = None

    def __init__(self, access_token, host):
        self.access_token = access_token
        self.host = utils.build_host(host)

    @property
    def api(self):
        if self._api is None:
            from api import Api
            self._api = Api(self)
        return self._api

    @property
    def chamada(self):
        return self.api.chamada
    
    @property
    def tts(self):
        return self.api.tts

    @property
    def audio(self):
        return self.api.audio

    @property
    def sms(self):
        return self.api.sms
    
    @property
    def conferencia(self):
        return self.api.conferencia