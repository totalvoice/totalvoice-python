# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Ura(Totalvoice):

    def __init__(self, cliente):
        super(Ura, self).__init__(cliente)

    def criar(self, nome, dados):
        """
        :Descrição:

        Função para criar uma ura.

        :Utilização:

        criar_ura()

        :Parâmetros:
        
        - nome:
        Nome para identificação

        - dados:
        Array de objetos com acao, opcao, menu e acao_dados. opção null = default. menu null = menu 1. Ação pode ser tts, audio, fila, transferir.
        """
        host = self.cliente.host + Routes.URA
        data = self.__build_ura(nome, dados)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def deletar(self, id):
        """
        :Descrição:

        Função para deletar um ramal.

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID da ura.
        """
        host = self.build_host(self.cliente.host, Routes.URA, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def editar(self, id, nome, dados):
        """
        :Descrição:

        Função para editar o ramal.

        :Utilização:

        editar(id, nome, dados)

        :Parâmetros:
        - id:
        ID da ura.

        - nome:
        Nome para identificação

        - dados:
        Array de objetos com acao, opcao, menu e acao_dados. opção null = default. menu null = menu 1. Ação pode ser tts, audio, fila, transferir.  
        """
        host = self.build_host(self.cliente.host, Routes.URA, [id])
        data = self.__build_ura(nome, dados)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def __build_ura(self, nome, dados):
        data = {}
        data.update({"nome": nome})
        data.update({"dados": dados})
        return json.dumps(data)
