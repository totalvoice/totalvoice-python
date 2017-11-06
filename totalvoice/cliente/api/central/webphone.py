# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Webphone(Totalvoice):

    def __init__(self, cliente):
        super(Webphone, self).__init__(cliente)

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
