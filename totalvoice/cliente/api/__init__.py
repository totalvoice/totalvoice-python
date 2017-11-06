from chamada import Chamada
from tts import Tts 
from sms import Sms
from audio import Audio
from conferencia import Conferencia
from minhaconta import MinhaConta
from composto import Composto
from conta import Conta
from central import Central

class Api(object):
    
    def __init__(self, cliente):
        self._cliente = cliente
        self._chamada        = None
        self._tts            = None
        self._sms            = None
        self._audio          = None
        self._conferencia    = None
        self._minha_conta    = None
        self._composto       = None
        self._conta          = None
        self._central        = None
    
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

    @property
    def composto(self):
        if self._composto is None:
            self._composto = Composto(self._cliente)
        return self._composto

    @property
    def conta(self):
        if self._conta is None:
            self._conta = Conta(self._cliente)
        return self._conta

    @property
    def central(self):
        if self._central is None:
            self._central = Central(self._cliente)
        return self._central