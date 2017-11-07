# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Conta(Totalvoice):

    def __init__(self, cliente):
        super(Conta, self).__init__(cliente)

    def criar_conta(self, nome, login, senha, cpf_cnpj=None, preco_fixo=None, preco_cel=None, preco_ramal=None, email_financeiro=None, nome_fantasia=None):
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
        host = self.cliente.host + Routes.CONTA
        data = self.__build_conta(nome, login, senha, cpf_cnpj, preco_fixo, preco_cel, preco_ramal, email_financeiro, nome_fantasia)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def deletar(self, id):
        """
        :Descrição:

        Função para deletar uma conta.

        :Utilização:

        deletar(id)

        :Parâmetros:

        - id:
        ID da conta ativa.
        """
        host = self.build_host(self.cliente.host, Routes.CONTA, [id])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
        
    def get_by_id(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma conta.

        :Utilização:

        get_by_id(id)

        :Parâmetros:

        - id:
        ID da conta ativa.
        """
        host = self.cliente.host + Routes.CONTA + "/" + id
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

    def get_relatorio(self):
        """
        :Descrição:
        
        Função para pegar o relatório de conta.

        :Utilização:

        get_relatorio()
        """
        host = self.build_host(self.cliente.host, Routes.CONTA, ["relatorio"])
        return self.get_request(host)


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
