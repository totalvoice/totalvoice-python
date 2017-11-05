from chamada import Chamada
from tts import Tts 
from sms import Sms
from audio import Audio
from conferencia import Conferencia
from minhaconta import MinhaConta

class Api(object):
    
    _cliente        = None
    _chamada        = None
    _tts            = None
    _sms            = None
    _audio          = None
    _conferencia    = None
    _minha_conta    = None

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
    
    @property
    def conferencia(self):
        if self._conferencia is None:
            self._conferencia = Conferencia(self._cliente)
        return self._conferencia

    @property
    def minha_conta(self):
        if self._minha_conta is None:
            self._minha_conta = MinhaConta(self._cliente)
        return self._minha_conta