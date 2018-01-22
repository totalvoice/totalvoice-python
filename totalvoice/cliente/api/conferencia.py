# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Conferencia(Totalvoice):

    def __init__(self, cliente):
        super(Conferencia, self).__init__(cliente)

    def cria_conferencia(self):
        """
        :Descrição:

        Essa é uma função para postar uma conferência

        :Utilização:

        cria_conferencia()

        """
        host = self.build_host(self.cliente.host, Routes.CONFERENCIA)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
    
    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma conferência ativa.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID da conferência ativa.
        """
        host = self.cliente.host + Routes.CONFERENCIA + "/" + id
        return self.get_request(host)

    def add_numero_conferencia(self, id_onferencia, numero, bina=None, gravar_audio=None):
        """
        :Descrição:

        Função para adicionar números de telefone na conferência ativa.

        :Utilização:

        add_numero_conferencia(idConferencia, numero, bina, gravar_audio)

        :Parâmetros:

        - idConferencia:
        ID da conferência ativa.

        - numero:
        Número do telefone que irá receber a chamada da conferência, formato DDD + Número exemplo: 4832830151

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato DDD + Número exemplo: 4832830151

        - gravar_audio:
        Flag que indica se o áudio deve ser gravado
        """
        host = self.cliente.host + Routes.CONFERENCIA + "/" + id_onferencia
        data = self.__buildConferencia(id_onferencia, numero, bina, gravar_audio)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def deletar(self, id):
        """
        :Descrição:

        Função para remover uma conferência ativa

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID da conferência.
        """
        host = self.build_host(self.cliente.host, Routes.CONFERENCIA, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def __buildConferencia(self, numero, bina, gravar_audio):
        """
        :Descrição:

        Função privada para realizar o build dos dados.
        """
        data = {}
        data.update({"numero": numero})
        data.update({"bina": bina})
        data.update({"gravar_audio": gravar_audio})
        return json.dumps(data)
