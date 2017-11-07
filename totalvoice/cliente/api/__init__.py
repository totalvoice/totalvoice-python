from __future__ import absolute_import
from totalvoice.cliente.api.chamada import Chamada
from totalvoice.cliente.api.tts import Tts 
from totalvoice.cliente.api.sms import Sms
from totalvoice.cliente.api.audio import Audio
from totalvoice.cliente.api.conferencia import Conferencia
from totalvoice.cliente.api.minhaconta import MinhaConta
from totalvoice.cliente.api.composto import Composto
from totalvoice.cliente.api.conta import Conta
from totalvoice.cliente.api.central.webphone import Webphone
from totalvoice.cliente.api.central.ramal import Ramal
from totalvoice.cliente.api.central.ura import Ura


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
        self._webphone       = None
        self._ramal          = None
        self._ura            = None
    
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
    def webphone(self):
        if self._webphone is None:
            self._webphone = Webphone(self._cliente)
        return self._webphone

    @property
    def ura(self):
        if self._ura is None:
            self._ura = Ura(self._cliente)
        return self._ura

    @property
    def ramal(self):
        if self._ramal is None:
            self._ramal = Ramal(self._cliente)
        return self._ramal
