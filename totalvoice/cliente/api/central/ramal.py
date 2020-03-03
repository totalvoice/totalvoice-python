# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Ramal(Totalvoice):

    def __init__(self, cliente):
        super(Ramal, self).__init__(cliente)

    def criar(self, dados):
        """
        :Descrição:

        Função para criar um ramal.

        :Utilização:

        criar(dados)

        :Parâmetros:
        
        - dados:
        Array de dados do ramal.
        """
        host = self.cliente.host + Routes.RAMAL
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(dados))
        return response.content

    def deletar(self, id):
        """
        :Descrição:

        Função para deletar um ramal.

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID do ramal.
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
        
    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de um ramal.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do ramal.
        """
        host = self.cliente.host + Routes.RAMAL + "/" + id
        return self.get_request(host)

    def editar(self, dados):
        """
        :Descrição:

        Função para editar o ramal.

        :Utilização:

        editar(dados)

        :Parâmetros:
        
        - dados:
        Array de dados do ramal.
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(dados))
        return response.content

    def get_relatorio(self):
        """
        :Descrição:
        
        Função para pegar o relatório de ramais.

        :Utilização:

        get_relatorio()
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL, ["relatorio"])
        return self.get_request(host)
    
    def editarRamalFila(self, id, dados):
        """
        :Descrição:

        Função para editar o ramal na fila.

        :Utilização:

        editar(dados)

        :Parâmetros:
        
        - dados:
        Array de dados do ramal.
        """
        host = self.cliente.host + Routes.RAMAL + "/" + str(id) + Routes.FILA
        print(host)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(dados))
        return response.content