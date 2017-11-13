# coding=utf-8
from totalvoice.cliente import Cliente

cliente = Cliente('SEU_TOKEN', 'api.totalvoice.com.br') #ex: api.totalvoice.com.br

nome_ura = "Ura Diurna";
json_ura = "{'nome': 'Ura Dinamica','dados':[{'acao':'tts','opcao':'','menu': 'menu 1','acao_dados':{'mensagem': 'Olá, bem vindo a totalvoice, digite 1 para suporte, 2 para financeiro'}},{'acao':'transfer','opcao':'1','menu': 'menu 1','acao_dados':{'numero_telefone': '4000'}},{'acao':'transfer','opcao':'2','menu': 'menu 1','acao_dados':{'numero_telefone': '4010'}}]}'}";
response = cliente.ura.criar(nome_ura, json_ura)
print (response)
