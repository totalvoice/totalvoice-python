# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Fila(Totalvoice):
    
    def __init__(self, cliente):
        super(Fila, self).__init__(cliente)

    def get_fila(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma fila

        :Utilização:

        get_fila(id)

        :Parâmetros:

        - id:
        ID da fila. 

        """
        host = self.build_host(self.cliente.host, Routes.FILA, [id])
        return self.get_request(host)

    def criar(self, nome, estrategia_ring, timeout_ring=None):
        """
        :Descrição:

        Função para criar uma fila

        :Utilização:

        criar(nome, estrategia_ring, timeout_ring)

        :Parâmetros:
        
        - nome:
        Nome da fila a ser criada

        - estrategia_ring:
        Multiplo para tocar todos ao mesmo tempo ou Distribuidor para tocar um ramal por vez.

        - timeout_ring
        Número em segundos para derrubar a chamada da fila.

        """
        host = self.build_host(self.cliente.host, Routes.FILA)
        data = self.__build_fila(nome, estrategia_ring, timeout_ring)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def add_ramal(self, id_fila, ramal_id):
        """
        :Descrição:

        Adiciona um ramal na fila

        :Utilização:

        add_ramal(id_fila, ramal_id)

        :Parâmetros:
        
        - id_fila:
        ID da fila

        - ramal_id:
        ID do ramal a ser adicionado na fila

        """
        host = self.build_host(self.cliente.host, Routes.FILA, [id_fila])
        data = {"ramal_id": ramal_id}
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(data))
        return response.content

    def editar(self, id, nome=None, estrategia_ring=None, timeout_ring=None):
        """
        :Descrição:

        Função para a fila.

        :Utilização:

        editar(nome, estrategia_ring, timeout_ring)

        :Parâmetros:
        
        - id:
        ID da fila a ser editada
        
        - nome:
        Nome da fila a ser criada

        - estrategia_ring:
        Multiplo para tocar todos ao mesmo tempo ou Distribuidor para tocar um ramal por vez.

        - timeout_ring
        Número em segundos para derrubar a chamada da fila.
        """
        dados = self.__build_fila(nome, estrategia_ring, timeout_ring)
        host = self.build_host(self.cliente.host, Routes.FILA, [id])
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=dados)
        return response.content

    def deleta_ramal(self, id, ramal_id):
        """
        :Descrição:

        Deleta ramal de uma fila

        :Utilização:

        deleta_ramal(id, ramal_id)

        :Parâmetros:

        - id:
        ID da fila.

        - ramal_id:
        ID do ramal.
        """
        host = self.build_host(self.cliente.host, Routes.FILA, [id, ramal_id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def get_fila_ramal(self, id, ramal_id):
        """
        :Descrição:

        Função para buscar as informações de uma fila e o ramal

        :Utilização:

        get_fila(id, ramal_id)

        :Parâmetros:

        - id:
        ID da fila.

        - ramal_id:
        ID do ramal.

        """
        host = self.build_host(self.cliente.host, Routes.FILA, [id, ramal_id])
        return self.get_request(host)
        
    def __build_fila(self, nome, estrategia_ring, timeout_ring):
        data = {}
        data.update({"nome": nome})
        data.update({"estrategia_ring": estrategia_ring})
        data.update({"timeout_ring": timeout_ring})
        return json.dumps(data)