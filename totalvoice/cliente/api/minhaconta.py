# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class MinhaConta(Totalvoice):

    def __init__(self, cliente):
        super(MinhaConta, self).__init__(cliente)

    def get_saldo(self):
        """
        :Descrição:

        Função para buscar saldo da sua conta.

        :Utilização:

        get_saldo()
        """
        host = self.build_host(self.cliente.host, Routes.SALDO)
        return self.get_request(host)

    def get_conta(self):
        """
        :Descrição:

        Função para buscar a sua conta.

        :Utilização:

        get_conta()
        """
        host = self.build_host(self.cliente.host, Routes.CONTA)
        return self.get_request(host)

    def editar_conta(self, nome, login, senha, cpf_cnpj=None, preco_fixo=None, preco_cel=None, preco_ramal=None, email_financeiro=None, nome_fantasia=None):
        """
        :Descrição:

        Função para editar a sua conta.

        :Utilização:

        editar_conta()

        :Parâmetros:
        
        - nome:
        Nome da conta.

        - login:
        Login da conta.

        - senha:
        Senha da conta;

        - cpf_cnpj:
        CPF ou CNPJ da conta.

        - preco_fixo:
        Preço de chamadas para fixo da conta.

        - preco_cel:
        Preço de chamadas para celulares da conta.

        - preco_ramal:
        Preço para ramais da conta.

        - email_financeiro:
        E-mail responsável pelo financeiro da conta.

        - nome_fantasia
        Nome fantasia da conta
        """
        host = self.build_host(self.cliente.host, Routes.CONTA)
        data = self.__build_conta(nome, login, senha, cpf_cnpj, preco_fixo, preco_cel, preco_ramal, email_financeiro, nome_fantasia)
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def get_recargas(self):
        """
        :Descrição:

        Função para as recargas da conta.

        :Utilização:

        get_recargas()
        """
        host = self.build_host(self.cliente.host, Routes.CONTA_RECARGAS)
        return self.get_request(host)

    def get_url_recarga(self, url_retorno):
        """
        :Descrição:

        Função para obter a url de recarga da conta.

        :Utilização:

        get_url_recarga()

        :Parâmetros:

        - url_retorno:
        URL para retorno depois da recarga ou ao cancelar.
        """
        data = {}
        data.update({"url_retorno": url_retorno})
        host = self.build_host(self.cliente.host, Routes.CONTA_URL_RECARGA, data=data)
        return self.get_request(host)

    def get_webhook(self):
        """
        :Descrição:

        Função para obter a lista webhook da conta.

        :Utilização:

        get_webhook()
        """
        host = self.build_host(self.cliente.host, Routes.WEBHOOK)
        return self.get_request(host)

    def delete_webhook(self, nome_webhook):
        """
        :Descrição:

        Função para deletar um webhook.

        :Utilização:

        get_webhook(nome_webhook)

        :Parâmetros:
        
        - nome_webhook:
        Nome do webhook.
        """
        host = self.build_host(self.cliente.host, Routes.WEBHOOK, [nome_webhook])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token), data=None)
        return response.content

    def editar_webhook(self, nome_webhook, url):
        """
        :Descrição:

        Função para deletar um webhook.

        :Utilização:

        editar_webhook(nome_webhook, url)

        :Parâmetros:
        
        - nome_webhook:
        Nome do webhook.

        - url:
        Url do webhook
        """
        host = self.build_host(self.cliente.host, Routes.WEBHOOK, [nome_webhook])
        data = {}
        data.update({"url" : url})
        response = requests.put(host, headers=utils.build_header(self.cliente.access_token), data=json.dumps(data))
        return response.content


    def __build_conta(self, nome, login, senha, cpf_cnpj, preco_fixo, preco_cel, preco_ramal, email_financeiro, nome_fantasia):
        data = {}
        data.update({"nome": nome})
        data.update({"login": login})
        data.update({"senha": senha})
        data.update({"cpf_cnpj": cpf_cnpj})
        data.update({"preco_fixo": preco_fixo})
        data.update({"preco_cel": preco_cel})
        data.update({"preco_ramal": preco_ramal})
        data.update({"email_financeiro": email_financeiro})
        data.update({"nome_fantasia": nome_fantasia})
        return json.dumps(data)
