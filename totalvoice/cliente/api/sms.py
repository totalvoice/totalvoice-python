# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Sms(Totalvoice):
    
    def __init__(self, cliente):
        super(Sms, self).__init__(cliente)

    def enviar(self, numero_destino, mensagem, resposta_usuario=None, multi_sms=None, data_criacao=None):
        """
        :Descrição:

        Função para enviar mensagens de texto.

        :Utilização:

        enviar(self, numero_destino, mensagem, resposta_usuario, multi_sms)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone que irá receber a mensagem, formato DDD + Número exemplo: 4832830151

        - mensagem:
        Mensagem de texto para ser enviada, limite: 160 caracteres não aceita acentos

        - resposta_usuario:
        Aguardar uma resposta do destinatário. true ou false. (Opcional)

        - multi_sms:
        Aceita SMS com mais de 160 char - ate 16.000. Envia multiplos sms para o mesmo numero (um a cada 160 char) e retorna array de ids. Default false. (Opcional)

        """
        host = self.build_host(self.cliente.host, Routes.SMS)
        data = self.__build_sms(numero_destino, mensagem, resposta_usuario, multi_sms, data_criacao)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar informações de SMS e respostas.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do sms.
        """
        host = self.build_host(self.cliente.host, Routes.SMS, [id])
        return self.get_request(host)

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de sms.

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
        host = self.build_host(self.cliente.host, Routes.SMS, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)

    def __build_sms(self, numero_destino, mensagem, resposta_usuario, multi_sms, data_criacao):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"mensagem": mensagem})
        data.update({"resposta_usuario": resposta_usuario})
        data.update({"multi_sms": multi_sms})
        data.update({"data_criacao": data_criacao})
        return json.dumps(data)
