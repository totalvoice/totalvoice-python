# coding=utf-8
from __future__ import absolute_import
from totalvoice.cliente.api.helper import utils

class Cliente(object):

    def __init__(self, access_token, host = None):
        self.access_token = access_token
        self.host = utils.build_host()
        self._api = None

    @property
    def api(self):
        """
        :Descrição:

        Acessa a API da Totalvoice

        :returns:

        API Totalvoice

        :rtype:

        totalvoice.cliente.api.Api
        """
        if self._api is None:
            from totalvoice.cliente.api import Api
            self._api = Api(self)
        return self._api

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
        return self.api.chamada

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
        return self.api.tts

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
        return self.api.audio

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
        return self.api.sms

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
        return self.api.conferencia

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
        return self.api.minha_conta

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
        return self.api.composto

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
        return self.api.conta

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
        return self.api.bina

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
        return self.api.ramal

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
        return self.api.ura

    @property
    def webphone(self):
        """
        :Descrição:

        Acessa Webphone da Totalvoice

        :returns:

        Webphone Totalvoice

        :rtype:

        totalvoice.cliente.api.central.webphone.Webphone
        """
        return self.api.webphone

    @property
    def did(self):
        """
        :Descrição:

        Gerenciamento de Dids

        :returns:

        Did Totalvoice

        :rtype:

        totalvoice.cliente.api.did.Did
        """
        return self.api.did

    @property
    def fila(self):
        """
        :Descrição:

        Gerenciamento de Fila

        :returns:

        Fila Totalvoice

        :rtype:

        totalvoice.cliente.api.fila.Fila
        """
        return self.api.fila
