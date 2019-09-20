# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Audio(Totalvoice):
    
    def __init__(self, cliente):
        super(Audio, self).__init__(cliente)

    def enviar(self, numero_destino, url_audio, resposta_usuario=None, bina=None, gravar_audio=None, detecta_caixa=None):
        """
        :Descrição:

        Essa é uma função para enviar um áudio para um número destino.

        :Utilização:

        enviar(numero_destino, url_audio, resposta_usuario, bina)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone destino.

        - url_audio:
        URL do áudio a ser enviado.

        - resposta_usuario:
        Booleano que informa se o usuário pode responder o áudio.

        - bina:
        Número de bina para a chamada de áudio.

        - gravar_audio:
        Opção para gravar áudio sim/não

        - detecta_caixa:
        Opção para detecção de caixa postal ao realizar a chamada
        """
        host = self.build_host(self.cliente.host, Routes.AUDIO)
        data = self.__build_audio(numero_destino, url_audio, resposta_usuario, bina, gravar_audio, detecta_caixa)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de um audio.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do audio.
        """
        host = self.cliente.host + Routes.AUDIO + "/" + id
        return self.get_request(host)
    
    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de áudios.

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
        host = self.build_host(self.cliente.host, Routes.AUDIO, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)

    def __build_audio(self, numero_destino, url_audio, resposta_usuario=None, bina=None, gravar_audio=None, detecta_caixa=None):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"url_audio": url_audio})
        data.update({"resposta_usuario": resposta_usuario})
        data.update({"bina": bina})
        data.update({"gravar_audio": gravar_audio})
        data.update({"detecta_caixa": detecta_caixa})
        return json.dumps(data)
