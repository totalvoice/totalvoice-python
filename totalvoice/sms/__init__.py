# coding=utf-8

from totalvoice.cliente import Cliente
from totalvoice.helper import utils
from totalvoice.helper.routes import Routes
import json, requests

class Sms(object):
    cliente = None

    def __init__(self, cliente):
        self.cliente = cliente

    def enviar_sms(self, numero_destino, mensagem, resposta_usuario=None, multi_sms=None):
        """
        :Descrição:

        Função para enviar mensagens de texto.

        :Utilização:

        enviar_sms(self, numero_destino, mensagem, resposta_usuario, multi_sms)

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
        host = self.cliente.host + Routes.SMS
        data = self.__buildSms(numero_destino, mensagem, resposta_usuario, multi_sms)
        response = requests.post(host, headers=utils.buildHeader(self.cliente.access_token), data=data)
        return response.content

    def __buildSms(self, numero_destino, mensagem, resposta_usuario, multi_sms):
        data = {}
        data.update({"numero_destino" : numero_destino})
        data.update({"mensagem" : mensagem})
        data.update({"resposta_usuario" : resposta_usuario})
        data.update({"multi_sms" : multi_sms})
        return json.dumps(data)

    def getSms(self, id):
        """
        :Descrição:

        Função para buscar informações de SMS e respostas.

        :Utilização:

        getSms(id)

        :Parâmetros:

        - id:
        ID do sms.
        """
        host = self.cliente.host + Routes.SMS + "/" + id
        return self.__get(host)

    def getRelatorioSms(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de sms.

        :Utilização:

        getRelatorioSms(data_inicio, data_fim)

        :Parâmetros:

        - data_inicio:
        Data início do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        - data_fim:
        Data final do relatório (2016-03-30T17:15:59-03:00)
        format UTC    

        """
        host = self.cliente.host + Routes.RELATORIO
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.__get(host, params)
        
    def __get(self, host, params = None):
        if params != None:
            response = requests.get(host, headers=headers, params=params)
        else:
            response = requests.get(host, headers=utils.buildHeader(self.cliente.access_token))
        return response.content
