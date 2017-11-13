from __future__ import absolute_import
import requests
from .helper import utils
class Totalvoice(object):

    def __init__(self, cliente):
        self.cliente = cliente
    
    def enviar(self, *args):
        raise NotImplementedError
    
    def get_by_id(self, id):
        raise NotImplementedError
    
    def editar(self, *args):
        raise NotImplementedError
    
    def get_relatorio(self, *args):
        raise NotImplementedError
        
    def deletar(self, id):
        raise NotImplementedError

    def get_request(self, host, params = None):
        if params != None:
            response = requests.get(host, headers=utils.build_header(self.cliente.access_token), params=params)
        else:
            response = requests.get(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def build_host(self, host, route, values=None):
        host += route
        if values is not None:
            for val in values:
                host +=  "/" + val
        return host
        