# coding=utf-8
from __future__ import absolute_import
from totalvoice.cliente.api.chamada import Chamada
from totalvoice.cliente.api.tts import Tts
from totalvoice.cliente.api.sms import Sms
from totalvoice.cliente.api.audio import Audio
from totalvoice.cliente.api.conferencia import Conferencia
from totalvoice.cliente.api.minhaconta import MinhaConta
from totalvoice.cliente.api.composto import Composto
from totalvoice.cliente.api.conta import Conta
from totalvoice.cliente.api.bina import Bina
from totalvoice.cliente.api.central.webphone import Webphone
from totalvoice.cliente.api.central.ramal import Ramal
from totalvoice.cliente.api.central.ura import Ura
from totalvoice.cliente.api.did import Did
from totalvoice.cliente.api.fila import Fila

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
        self._bina           = None
        self._webphone       = None
        self._ramal          = None
        self._ura            = None
        self._did            = None
        self._fila           = None

    @property
    def chamada(self):
        """
        :Descrição:
        Acessa Chamada da Totalvoice

        :returns:

        Chamada Totalvoice

        :rtype:

        totalvoice.cliente.api.chamada.Chamada
        """
        if self._chamada is None:
            self._chamada = Chamada(self._cliente)
        return self._chamada

    @property
    def tts(self):
        """
        :Descrição:

        Acessa TTS da Totalvoice

        :returns:

        TTS Totalvoice

        :rtype:

        totalvoice.cliente.api.tts.Tts
        """
        if self._tts is None:
            self._tts = Tts(self._cliente)
        return self._tts

    @property
    def sms(self):
        """
        :Descrição:

        Acessa SMS da Totalvoice

        :returns:

        SMS Totalvoice

        :rtype:

        totalvoice.cliente.api.sms.Sms
        """
        if self._sms is None:
            self._sms = Sms(self._cliente)
        return self._sms

    @property
    def audio(self):
        """
        :Descrição:

        Acessa Audio da Totalvoice

        :returns:

        Audio Totalvoice

        :rtype:

        totalvoice.cliente.api.audio.Audio
        """
        if self._audio is None:
            self._audio = Audio(self._cliente)
        return self._audio

    @property
    def conferencia(self):
        """
        :Descrição:

        Acessa Conferência da Totalvoice

        :returns:

        Conferência Totalvoice

        :rtype:

        totalvoice.cliente.api.conferencia.Conferencia
        """
        if self._conferencia is None:
            self._conferencia = Conferencia(self._cliente)
        return self._conferencia

    @property
    def minha_conta(self):
        """
        :Descrição:

        Acessa Minha Conta da Totalvoice

        :returns:

        MinhaConta Totalvoice

        :rtype:

        totalvoice.cliente.api.minhaconta.MinhaConta
        """
        if self._minha_conta is None:
            self._minha_conta = MinhaConta(self._cliente)
        return self._minha_conta

    @property
    def composto(self):
        """
        :Descrição:

        Acessa Composto da Totalvoice

        :returns:

        Composto Totalvoice

        :rtype:

        totalvoice.cliente.api.composto.Composto
        """
        if self._composto is None:
            self._composto = Composto(self._cliente)
        return self._composto

    @property
    def conta(self):
        """
        :Descrição:

        Acessa Conta da Totalvoice

        :returns:

        Conta Totalvoice

        :rtype:

        totalvoice.cliente.api.conta.Conta
        """
        if self._conta is None:
            self._conta = Conta(self._cliente)
        return self._conta

    @property
    def bina(self):
        """
        :Descrição:

        Acessa Bina da Totalvoice

        :returns:

        Bina Totalvoice

        :rtype:

        totalvoice.cliente.api.bina.Bina
        """
        if self._bina is None:
            self._bina = Bina(self._cliente)
        return self._bina

    @property
    def webphone(self):
        """
        :Descrição:

        Acessa Webphone da Totalvoice

        :returns:

        WEbphone Totalvoice

        :rtype:

        totalvoice.cliente.api.central.webphone.Webphone
        """
        if self._webphone is None:
            self._webphone = Webphone(self._cliente)
        return self._webphone

    @property
    def ura(self):
        """
        :Descrição:

        Acessa Ura da Totalvoice

        :returns:

        Ura Totalvoice

        :rtype:

        totalvoice.cliente.api.central.ura.Ura
        """
        if self._ura is None:
            self._ura = Ura(self._cliente)
        return self._ura

    @property
    def ramal(self):
        """
        :Descrição:

        Acessa Ramal da Totalvoice

        :returns:

        Ramal Totalvoice

        :rtype:

        totalvoice.cliente.api.central.ramal.Ramal
        """
        if self._ramal is None:
            self._ramal = Ramal(self._cliente)
        return self._ramal

    @property
    def did(self):
        """
        :Descrição:

        Gerenciamento de dids

        :returns:

        Did Totalvoice

        :rtype:

        totalvoice.cliente.api.did.Did
        """
        if self._did is None:
            self._did = Did(self._cliente)
        return self._did

    @property
    def fila(self):
        """
        :Descrição:

        Gerenciamento de filas

        :returns:

        Fila Totalvoice

        :rtype:

        totalvoice.cliente.api.fila.Fila
        """
        if self._fila is None:
            self._fila = Fila(self._cliente)
        return self._fila
