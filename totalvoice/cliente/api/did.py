# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Did(Totalvoice):
    
    def __init__(self, cliente):
        super(Did, self).__init__(cliente)

    def get_my_dids(self):
        """
        :Descrição:

        Função para buscar todos os dids seus dids

        :Utilização:

        get_my_dids()

        """
        host = self.build_host(self.cliente.host, Routes.DID)
        return self.get_request(host)

    def get_estoque(self):
        """
        :Descrição:

        Função para buscar a lista de dids no estoque

        :Utilização:

        get_my_dids()

        """
        host = self.build_host(self.cliente.host, Routes.DID_ESTOQUE)
        return self.get_request(host)

    def compra_estoque(self, did_id):
        """
        :Descrição:

        Essa é uma função que compra um número (did) do estoque

        :Utilização:

        compra_estoque(did_id)

        :Parâmetros:
        
        - did_id:
        ID do did que deseja comprar
        """
        host = self.build_host(self.cliente.host, Routes.DID_ESTOQUE)
        data = {}
        data.update({"did_id": did_id})
        data = json.dumps(data)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def editar(self, did_id, ura_id=None, ramal_id=None):
        """
        :Descrição:

        Função para editar o seu did.

        :Utilização:

        editar(did_id, ura_id, ramal_id)

        :Parâmetros:
        
        - did_id:
        ID do did que deseja editar.
        
        - ura_id:
        Ura ID para atrlar ao did.

        - ramal_id:
        Ramal ID para atrlar ao did.
        """
        data = {}
        data.update({"did_id": did_id})
        data.update({"ura_id": ura_id})
        data.update({"ramal_id": ramal_id})
        host = self.build_host(self.cliente.host, Routes.DID)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(data))
        return response.content

    def deletar(self, id):
        """
        :Descrição:

        Função para remover o did da conta.

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID do did.
        """
        host = self.build_host(self.cliente.host, Routes.DID, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def get_chamada_recebida(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma chamada recebida.

        :Utilização:

        get_chamada_recebida(id)

        :Parâmetros:

        - id:
        ID da chamada ativa.
        """
        host = self.cliente.host + Routes.DID_CHAMADA + "/" + id
        return self.get_request(host)

    def get_relatorio(self, data_inicio, data_fim, id=None):
        """
        :Descrição:
        
        Função para pegar o relatório de chamadas recebidas.

        :Utilização:

        get_relatorio(data_inicio, data_fim, id)

        :Parâmetros:

        - data_inicio:
        Data início do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        - data_fim:
        Data final do relatório (2016-03-30T17:15:59-03:00)
        format UTC
        
        - id:
        Se preenchido busca os dados daquele número específico.

        """
        host = self.build_host(self.cliente.host, Routes.DID, ["relatorio"])
        if id is not None:
            host = host + id
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)