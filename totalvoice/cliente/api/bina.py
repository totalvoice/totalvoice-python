# coding=utf-8
from __future__ import absolute_import
from .helper import utils
from .helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests


class Bina(Totalvoice):
    
    def __init__(self, cliente):
        super(Bina, self).__init__(cliente)

    def enviar(self, telefone):
        """
        :Descrição:

        Envia um número de telefone para que receba um código via SMS (celular) ou TSS (fixo)

        :Utilização:

        enviar(telefone)

        :Parâmetros:
        
        - telefone:
        Número do telefone que irá receber a Chamada(fixo) ou SMS(móvel) com o código para validação
        """
        host = self.build_host(self.cliente.host, Routes.BINA)
        data = self.__build_bina(telefone)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def validar(self, codigo, telefone):
        """
        :Descrição:

        Você deve informar o código recebido no celular (SMS) ou telefone (TTS) informados no método POST, para realizarmos a validação

        :Utilização:

        validar(codigo, telefone)

        :Parâmetros:

        - codigo:
        Código que será validado.

        - telefone:
        Telefone que será validado.
        """
        host = self.cliente.host + Routes.BINA
        params = (('codigo', codigo),('telefone', telefone),)
        return self.get_request(host, params)

    def excluir(self, telefone):
        """
        :Descrição:

        Apaga o número de telefone (Bina) cadastrado na Conta

        :Utilização:

        excluir(telefone)

        :Parâmetros:

        - telefone:
        Telefone (bina) que será removido.
        """
        host = self.build_host(self.cliente.host, Routes.BINA, [telefone])
        response = requests.delete(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
    
    def get_relatorio(self):
        """
        :Descrição:
        
        Busca os telefones (Bina) cadastrados na Conta

        :Utilização:

        get_relatorio()  

        """
        host = self.build_host(self.cliente.host, Routes.BINA, ["relatorio"])
        return self.get_request(host)

    def __build_bina(self, telefone):
        data = {}
        data.update({"telefone": telefone})
        return json.dumps(data)
