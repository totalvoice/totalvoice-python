# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Tts(Totalvoice):

    def __init__(self, cliente):
        super(Tts, self).__init__(cliente)

    def enviar(self, numero_destino, mensagem, velocidade=None, resposta_usuario=None, tipo_voz=None, bina=None, gravar_audio=None, detecta_caixa=None):
        """
        :Descrição:

        Função para enviar TTS (Text-to-speech)

        :Utilização:

        enviar(self, numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone que irá receber a mensagem, formato DDD + Número exemplo: 4832830151.

        - mensagem:
        Mensagem que será lida para o destinatário.

        - valocidade
        De -10 a 10. Onde -10=muito lento, 0=normal e 10=muito rápido.

        - resposta_usuario:
        Aguardar uma resposta do destinatário. true ou false.

        - tipo_voz:
        Informe a sigla do idioma concatenado ao nome do personagem que vai falar. Ex: br-Ricardo, br-Vitoria.

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato DDD + Número exemplo: 4832830151.

        - gravar_audio:
        Opção para gravar áudio sim/não

        - detecta_caixa:
        Opção para detecção de caixa postal ao realizar a chamada
        """
        host = self.build_host(self.cliente.host, Routes.TTS)
        data = self.__build_tts(numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina, gravar_audio, detecta_caixa)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar informações de TTS e respostas.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do tts.
        """
        host = self.build_host(self.cliente.host, Routes.TTS, [id])
        return self.get_request(host)

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de tts.

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
        host = self.build_host(self.cliente.host, Routes.TTS, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)

    def __build_tts(self, numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina, gravar_audio, detecta_caixa):
        data = {}
        data.update({"numero_destino": numero_destino})
        data.update({"mensagem": mensagem})
        data.update({"velocidade": velocidade})
        data.update({"resposta_usuario": resposta_usuario})
        data.update({"tipo_voz": tipo_voz})
        data.update({"bina": bina})
        data.update({"gravar_audio": gravar_audio})
        data.update({"detecta_caixa": detecta_caixa})
        return json.dumps(data)
