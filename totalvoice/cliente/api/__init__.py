from chamada import Chamada
from tts import Tts 
from sms import Sms
from audio import Audio


class Api(object):
    
    _cliente    = None
    _chamada    = None
    _tts        = None
    _sms        = None
    _audio      = None

    def __init__(self, cliente):
        self._cliente = cliente
    
    @property
    def chamada(self):
        if self._chamada is None:
            self._chamada = Chamada(self._cliente)
        return self._chamada
    
    @property
    def tts(self):
        if self._tts is None:
            self._tts = Tts(self._cliente)
        return self._tts
    
    @property
    def sms(self):
        if self._sms is None:
            self._sms = Sms(self._cliente)
        return self._sms

    @property
    def audio(self):
        if self._audio is None:
            self._audio = Audio(self._cliente)
        return self._audio