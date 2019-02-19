# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class ValidaNumero(Totalvoice):

    def __init__(self, cliente):
        super(ValidaNumero, self).__init__(cliente)

    def enviar(self, numero_destino, gravar_audio=None, bina=None, max_tentativas=None):
        """
        :Descrição:

        Função para uma validação de número

        :Utilização:

        enviar(self, numero_destino, gravar_audio, bina, max_tentativas)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone que irá receber a mensagem, formato DDD + Número exemplo: 4832830151.

        - gravar_audio:
        Grava ligacao

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato DDD + Número exemplo: 4832830151.

        - max_tentativas:
        Número máximo de tentativas de validação. Default é 1 e o máximo é 5.

        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO)
        data = self.__build_validanumero(numero_destino, gravar_audio, bina, max_tentativas)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar validação pelo ID.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do tts.
        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO, [id])
        return self.get_request(host)

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de validação

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

    def __build_validanumero(self, numero_destino, gravar_audio, bina, max_tentativas):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"gravar_audio": gravar_audio})
        data.update({"bina": bina})
        data.update({"max_tentativas": max_tentativas})
        return json.dumps(data)
