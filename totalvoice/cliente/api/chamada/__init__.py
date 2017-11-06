# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Chamada(Totalvoice):
    
    def __init__(self, cliente):
        super(Chamada, self).__init__(cliente)

    def enviar(self, numero_origem, numero_destino, data_criacao=None, gravar_audio=False, bina_origem=None, bina_destino=None, tags=None):
        """
        :Descrição:

        Essa é uma função para realizar uma chamada
        entre dois números de telefone.

        :Utilização:

        enviar(numero_origem, numero_destino, data_criacao, gravar_audio, bina_origem, bina_destino, tags)

        :Parâmetros:
        
        - numero_origem:
        Número do telefone de origem (Perna A).

        - numero_destino:
        Número do telefone destino (Perna B).

        - data_criacao:
        Data de criação da chamada, serve para
        disparar uma chamada na data e hora desejada.

        - gravar_audio:
        Grava o audio da chamada.

        - bina_origem:
        Número de bina que vai aparecer quando tocar o numero origem.

        - bina_destino:
        Número de bina que vai aparecer quando tocar o numero destino.

        - tags:
        Campo para passar informações para capturar em webhooks.
        """
        host = self.build_host(self.cliente.host, Routes.CHAMADA)
        data = self.__buildChamada(numero_origem, numero_destino, data_criacao, gravar_audio, bina_origem, bina_destino, tags)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def escutaChamada(self, id, numero, modo):
        """
        (BETA - EM TESTES)
        ----------

        :Descrição:
        
        Função para escutar uma chamada, passa o id, número e modo e é possível escutar a chamada.

        :Utilização:
        
        escutaChamada(id, numero, modo)

        :Parâmetros:

        - id:
            ID da chamada ativa.

        - numero:
            Número do seu telefone.

        - modo:
            Modo de escuta: 1=escuta, 2=sussurro, 3=conferência.
        """
        host = self.build_host(self.cliente.host, Routes.CHAMADA, [id, "escuta"])
        data = {}
        data.update({"numero" : numero})
        data.update({"modo" : modo})
        data = json.dumps(data)
        requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)

    def deletar(self, id):
        """
        :Descrição:

        Função para deletar uma chamada ativa.

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID da chamada ativa.
        """
        host = self.build_host(self.cliente.host, Routes.CHAMADA, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
    
    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma chamada ativa.

        :Utilização:

        getChamada(id)

        :Parâmetros:

        - id:
        ID da chamada ativa.
        """
        host = self.cliente.host + Routes.CHAMADA + "/" + id
        return self.get_request(host)

    def getGravacaoChamada(self, id):
        """
        :Descrição:

        Função para pegar a URL de gravação da chamada.

        :Utilização:

        getGravacaoChamada(id)

        :Parâmetros:

        - id:
        ID da chamada ativa.
        """
        host = self.build_host(self.cliente.host, Routes.CHAMADA, [id, "gravacao"])
        return self.get_request(host)

    def get_relatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de chamadas.

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
        host = self.build_host(self.cliente.host, Routes.CHAMADA, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.get_request(host, params)

    def __buildChamada(self, numero_origem, numero_destino, data_criacao, gravar_audio, bina_origem, bina_destino, tags):
        data = {}
        data.update({"numero_origem": numero_origem})
        data.update({"numero_destino": numero_destino})
        data.update({"data_criacao": data_criacao})
        data.update({"gravar_audio": gravar_audio})
        data.update({"bina_origem": bina_origem})
        data.update({"bina_destino": bina_destino})
        data.update({"tags": tags})
        return json.dumps(data)
