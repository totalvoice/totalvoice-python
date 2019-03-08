# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class ValidaNumero(Totalvoice):

    def __init__(self, cliente):
        super(ValidaNumero, self).__init__(cliente)

<<<<<<< HEAD
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
=======
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
>>>>>>> master

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
<<<<<<< HEAD
        
        Função para pegar o relatório de validação
=======

        Função para pegar o relatório de compostos.
>>>>>>> master

        :Utilização:

        get_relatorio(data_inicio, data_fim)

        :Parâmetros:

        - data_inicio:
        Data início do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        - data_fim:
        Data final do relatório (2016-03-30T17:15:59-03:00)
<<<<<<< HEAD
        format UTC    
=======
        format UTC
>>>>>>> master

        """
        host = self.build_host(self.cliente.host, Routes.VALIDA_NUMERO, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)
<<<<<<< HEAD

    def __build_validanumero(self, numero_destino, gravar_audio, bina, max_tentativas):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"gravar_audio": gravar_audio})
        data.update({"bina": bina})
        data.update({"max_tentativas": max_tentativas})
        return json.dumps(data)
=======
>>>>>>> master
