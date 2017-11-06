# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Central(Totalvoice):

    def __init__(self, cliente):
        super(Central, self).__init__(cliente)

    def criar_ramal(self, dados):
        """
        :Descrição:

        Função para criar um ramal.

        :Utilização:

        criar_ramal()

        :Parâmetros:
        
        - dados:
        Array de dados do ramal.
        """
        host = self.cliente.host + Routes.RAMAL
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(dados))
        return response.content

    def deletar_ramal(self, id):
        """
        :Descrição:

        Função para deletar um ramal.

        :Utilização:

        deletar_ramal(id)

        :Parâmetros:

        - id:
        ID do ramal.
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
        
    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de um ramal.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID do ramal.
        """
        host = self.cliente.host + Routes.RAMAL + "/" + id
        return self.get_request(host)

    def editar_ramal(self, dados):
        """
        :Descrição:

        Função para editar o ramal.

        :Utilização:

        editar_conta()

        :Parâmetros:
        
        - dados:
        Array de dados do ramal.
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(dados))
        return response.content

    def get_relatorio_ramal(self):
        """
        :Descrição:
        
        Função para pegar o relatório de ramais.

        :Utilização:

        get_relatorio_ramal()
        """
        host = self.build_host(self.cliente.host, Routes.RAMAL, ["relatorio"])
        return self.get_request(host)

    def criar_ura(self, nome, dados):
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

    def deletar_ura(self, id):
        """
        :Descrição:

        Função para deletar um ramal.

        :Utilização:

        deletar_ura(id)

        :Parâmetros:

        - id:
        ID da ura.
        """
        host = self.build_host(self.cliente.host, Routes.URA, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content

    def editar_ura(self, id, nome, dados):
        """
        :Descrição:

        Função para editar o ramal.

        :Utilização:

        editar_ura()

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

    def get_webphone(self, tipo="floating", id_ramal=None, ramal=None, ligar_para=None, fechar_fim=None):
        """
        :Descrição:
        
        Função para pegar o relatório de ramais.

        :Utilização:

        get_webphone()
        
        :Parâmetros:
        - tipo:
        Embedded = embutido no site, floating = popup, hidden = sem interface e com funcoes de callback. veja documentacao de exemplo no blog.

        - id_ramal:
        ID do ramal para pré-configurar o widget

        - ramal:
        Número do ramal para pré-configurar o widget.

        - ligar_para:
        Abrir o webphone ligando para o número, formato DDD + Número exemplo: 4832830151.

        - fechar_fim:
        Fechar a janela do webphone quando a chamada for encerrada?
        """
        host = self.build_host(self.cliente.host, Routes.WEBPHONE)
        params = (('tipo', tipo),('id_ramal', id_ramal), ('ramal', ramal), ('ligar_para', ligar_para), ('fechar_fim', fechar_fim))
        return self.get_request(host, params)

    def __build_ura(self, nome, dados):
        data = {}
        data.update({"nome" : nome})
        data.update({"dados" : dados})
        return json.dumps(data)