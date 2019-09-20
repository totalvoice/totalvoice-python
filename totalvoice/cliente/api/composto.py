# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Composto(Totalvoice):
    
    def __init__(self, cliente):
        super(Composto, self).__init__(cliente)

    def enviar(self, numero_destino, dados, bina=None, tags=None, gravar_audio=None, detecta_caixa=None):
        """
        :Descrição:

        Essa é uma função para enviar um composto de dados para um número destino.

        :Utilização:

        enviar(numero_destino, dados, bina, tags)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone destino.

        - dados:
        Array de objetos com acao e acao_dados , podendo ser TTS, Audio ou Transferir cada um deles. 
        O campo opcao é opcional, se configurado, só aciona a ação se a opção tiver sido digitada - DTMF.

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato 
        DDD + Número exemplo: 4832830151

        - tags:
        Tags para uso geral

        - gravar_audio:
        Opção para gravar áudio sim/não

        - detecta_caixa:
        Opção para detecção de caixa postal ao realizar a chamada
        """
        
        host = self.build_host(self.cliente.host, Routes.COMPOSTO)
        data = self.__build_composto(numero_destino, dados, bina, tags, gravar_audio, detecta_caixa)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de um composto enviado.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do composto.
        """
        host = self.cliente.host + Routes.COMPOSTO + "/" + id
        return self.get_request(host)
    
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
        host = self.build_host(self.cliente.host, Routes.COMPOSTO, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)

    def __build_composto(self, numero_destino, dados, bina, tags, gravar_audio, detecta_caixa):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"dados": dados})
        data.update({"bina": bina})
        data.update({"tags": tags})
        data.update({"gravar_audio": gravar_audio})
        data.update({"detecta_caixa": detecta_caixa})
        return json.dumps(data)
