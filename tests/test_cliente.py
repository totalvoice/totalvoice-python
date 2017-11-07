import pytest
from totalvoice.cliente import Cliente
from totalvoice.cliente.api import Api
from totalvoice.cliente.api.chamada import Chamada

class TestCliente(object):
    
    def setup(self):
        self.cliente = Cliente("token", "host")     
    
    def test_cliente(self):
        assert self.cliente.host == "https://host"
        assert self.cliente.access_token == "token"
    
    def test_api(self):
        assert isinstance(self.cliente.api, Api)
        assert isinstance(self.cliente.api.chamada, Chamada)