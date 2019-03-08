# Totalvoice-python
Cliente em Python para API da Totalvoice

[![Build Status](https://travis-ci.org/totalvoice/totalvoice-python.svg?branch=master)](https://travis-ci.org/totalvoice/totalvoice-python)

## Pré requisitos

```
$ pip install totalvoice
```

## Como utilizar (how to)

Segue abaixo a forma de utilização dos métodos da API da totalvoice!

### Chamadas
Módulo responsável por criação de chamadas, relatórios de chamadas, url da gravação, etc.


```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Cria chamada
numero_origem = "48999999999"
numero_destino = "48900000000"
response = cliente.chamada.enviar(numero_origem, numero_destino)
print(response)

#Get chamada
id = "1958"
response = cliente.chamada.get_by_id(id)
print(response)

#Get URL da chamada
id = "1958"
response = cliente.chamada.get_gravacao_chamada(id) 
print(response)

#Relatório de chamada
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = cliente.chamada.get_relatorio(data_inicio, data_fim)
print(response)

#Escutar chamada (BETA)
id_chamada = "1958"
numero = "48999999999"
modo = 1 #1=escuta, 2=sussurro, 3=conferência.
response = cliente.chamada.escuta_chamada(id_chamada, numero, modo)
print(response)

#Deletar
id = "1958"
response = cliente.chamada.deletar(id)
print(response)


```

### SMS
Módulo responsável por criação de SMS, relatórios.

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Cria sms
numero_destino = "48999999999"
mensagem = "teste envio sms"
response = cliente.sms.enviar(numero_destino, mensagem)
print(response)

#Get sms
id = "1958"
response = cliente.sms.get_by_id(id)
print(response)

#Relatório de sms
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = cliente.sms.get_relatorio(data_inicio, data_fim)
print(response)

```

### Audio
Módulo responsável por criação de Audios.

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Cria audio
numero = "48999999999"
url_audio = "http://fooo.bar"
response = cliente.audio.enviar(numero, url_audio)
print(response)

#Get audio
id = "1958"
response = cliente.audio.get_by_id(id)
print(response)

#Relatório de audio
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = cliente.audio.get_relatorio(data_inicio, data_fim)
print(response)

```

### TTS
Módulo responsável por criação de Audios.

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Cria TTS
numero_destino = "48999999999"
mensagem = "Olá, esta mensagem será lida"
response = cliente.tts.enviar(numero_destino, mensagem)
print(response)

#Get TTS
id = "1958"
response = cliente.tts.get_by_id(id)
print(response)

#Relatório de TTS
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = cliente.tts.get_relatorio(data_inicio, data_fim)
print(response)

```

### Conferência
Módulo responsável por criação de Conferências.

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Cria conferência
response = cliente.conferencia.cria_conferencia()
print(response)

#Get conferência
id = "1958"
response = cliente.conferencia.get_by_id(id)
print(response)

#Add número na conferência
id_conferencia = "15"
numero = "48999999999"
response = cliente.conferencia.add_numero_conferencia(id_conferencia, numero)
print(response)

```

### DID
Módulo responsável pelo gerenciamento de did (números de telefone)

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#Lista todos os dids disponíveis em estoque
response = cliente.did.get_estoque()
print(response)

#Compra did do estoque
did_id = "1958"
response = cliente.did.compra_estoque(did_id)
print(response)

#Lista todos os dids que a conta possuí
response = cliente.did.get_my_dids()
print(response)

#Edita os dados do seu DID, podendo alterar o ramal id e a ura id
did_id = "1"
ramal_id = None
ura_id = "10"
response = cliente.did.editar(did_id, ura_id, ramal_id)
print(response)

#Remove o did da conta
did_id = "1"
response = cliente.did.deletar(did_id)
print(response)

#Lista os dados de uma chamada recebida
chamada_id = "5599"
response = cliente.did.get_chamada_recebida(chamada_id)
print(response)

```

### Valida Número
Módulo responsável por validar se o número de telefone informado está ativo ou inativo

```python
from totalvoice.cliente import Cliente

cliente = Cliente("{{access-token}}", 'HOST') #ex: api.totalvoice.com.br

#cria um registro validaNumero que irá checar se o número é válido
response = cliente.valida_numero.criar("4811111111");
print(response)

#Retona um registro de validaNumero
valida_numero_id = "1958"
response = cliente.valida_numero.get_valida_numero(valida_numero_id);
print(response)

#Retorna um relatório de validaNumero por período
response = cliente.valida_numero.get_relatorio('2019-01-01','2019-05-05');
print(response)

```


## Licença

MIT
