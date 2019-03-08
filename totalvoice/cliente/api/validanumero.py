# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class ValidaNumero(Totalvoice):

    def __init__(self, cliente):
        super(ValidaNumero, self).__init__(cliente)

    def get_valida_numero(self, id):
        """
        :Descrição:

        Função para buscar as informações de um ValidaNumero

        :Utilização:

        get_valida_numero(id)

        :Parâmetros:

        - id:
        ID da do ValidaNumero.

        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO, [str(id)])
        return self.get_request(host)

    def criar(self, numero_destino):
        """
        :Descrição:

        Função para criar um ValidaNumero que irá validar se o número
        fornecido é um número ativo ou inativo.

        :Utilização:

        criar(numero_destino)

        :Parâmetros:

        - numero_destino:
        Número do telefone que será validado.
        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO)

        data = {}
        data.update({"numero_destino" : numero_destino})
        data = json.dumps(data)

        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:

        Função para pegar o relatório de compostos.

        :Utilização:

        get_relatorio(data_inicio, data_fim)

        :Parâmetros:

        - data_inicio:
        Data início do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        - data_fim:
        Data final do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)
