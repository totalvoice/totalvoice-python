import pytest
from totalvoice.cliente import Cliente
from totalvoice.cliente.api import *

class TestCliente(object):
    
    def setup(self):
        self.cliente = Cliente("token", "host")     
    
    def test_cliente(self):
        assert self.cliente.host is not None
        assert self.cliente.host == "https://host"
        assert self.cliente.access_token is not None
        assert self.cliente.access_token == "token"
    
    def test_api(self):
        assert self.cliente.access_token is not None
        assert isinstance(self.cliente.api, Api)
    
    def test_api_chamada(self):
        assert self.cliente.api.chamada is not None
        assert isinstance(self.cliente.api.chamada, Chamada)
    
    def test_api_tts(self):
        assert self.cliente.api.tts is not None
        assert isinstance(self.cliente.api.tts, Tts)

    def test_api_audio(self):
        assert self.cliente.api.audio is not None
        assert isinstance(self.cliente.api.audio, Audio)

    def test_api_sms(self):
        assert self.cliente.api.sms is not None
        assert isinstance(self.cliente.api.sms, Sms)

    def test_api_composto(self):
        assert self.cliente.api.composto is not None
        assert isinstance(self.cliente.api.composto, Composto)

    def test_api_conferencia(self):
        assert self.cliente.api.conferencia is not None
        assert isinstance(self.cliente.api.conferencia, Conferencia)

    def test_api_minhaconta(self):
        assert self.cliente.api.minha_conta is not None
        assert isinstance(self.cliente.api.minha_conta, MinhaConta)

    def test_api_conta(self):
        assert self.cliente.api.conta is not None
        assert isinstance(self.cliente.api.conta, Conta)

    def test_api_bina(self):
        assert self.cliente.api.bina is not None
        assert isinstance(self.cliente.api.bina, Bina)

    def test_api_webphone(self):
        assert self.cliente.api.webphone is not None
        assert isinstance(self.cliente.api.webphone, Webphone)

    def test_api_ramal(self):
        assert self.cliente.api.ramal is not None
        assert isinstance(self.cliente.api.ramal, Ramal)

    def test_api_ura(self):
        assert self.cliente.api.ura is not None
        assert isinstance(self.cliente.api.ura, Ura)