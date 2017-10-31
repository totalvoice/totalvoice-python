# Totalvoice-python
Cliente em Python para API da Totalvoice

## Pré requisitos

```
$ pip install totalvoice
```

## Como utilizar (how to)

Segue abaixo a forma de utilização dos métodos da API da totalvoice!

### Chamadas
Módulo responsável por criação de chamadas, relatórios de chamadas, url da gravação, etc.


```python
from totalvoice import *

cliente = Cliente("SEU_TOKEN", 'HOST') #ex: api.totalvoice.com.br
chamada = Chamada(cliente)

#Cria chamada
numero_origem = "48999999999"
numero_destino = "48900000000"
response = chamada.enviar(numero_origem, numero_destino)
print(response)

#Get chamada
id = "1958"
response = chamada.getById(id)
print(response)

#Get URL da chamada
id = "1958"
response = chamada.getGravacaoChamada(id) 
print(response)

#Relatório de chamada
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = chamada.getRelatorio(data_inicio, data_fim)
print(response)

#Escutar chamada (BETA)
id_chamada = "1958"
numero = "48999999999"
modo = 1 #1=escuta, 2=sussurro, 3=conferência.
response = chamada.escutaChamada(id_chamada, numero, modo)
print(response)

#Deletar
id = "1958"
response = chamada.deletar(id)
print(response)


```

### SMS
Módulo responsável por criação de SMS, relatórios.

```python
from totalvoice import *

cliente = Cliente("SEU_TOKEN", 'HOST') #ex: api.totalvoice.com.br
sms = Sms(cliente)

#Cria sms
numero_destino = "48999999999"
mensagem = "teste envio sms"
response = sms.enviar(numero_destino, mensagem)
print(response)

#Get sms
id = "1958"
response = sms.getById(id)
print(response)

#Relatório de sms
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = sms.getRelatorio(data_inicio, data_fim)
print(response)

```

### Audio
Módulo responsável por criação de Audios.

```python
from totalvoice import *

cliente = Cliente("SEU_TOKEN", 'HOST') #ex: api.totalvoice.com.br
audio = Audio(cliente)

#Cria audio
numero = "48999999999"
url_audio = "http://fooo.bar"
response = audio.enviar(numero, url_audio)
print(response)

#Get audio
id = "1958"
response = audio.getById(id)
print(response)

#Relatório de audio
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = audio.getRelatorio(data_inicio, data_fim)
print(response)

```

### TTS
Módulo responsável por criação de Audios.

```python
from totalvoice import *

cliente = Cliente("SEU_TOKEN", 'HOST') #ex: api.totalvoice.com.br
tts = Tts(cliente)

#Cria audio
numero_destino = "48999999999"
mensagem = "Olá, esta mensagem será lida"
response = tts.enviar(numero_destino, mensagem)
print(response)

#Get audio
id = "1958"
response = tts.getById(id)
print(response)

#Relatório de audio
data_inicio = "2016-03-30T17:15:59-03:00"
data_fim = "2016-03-30T17:15:59-03:00"
response = tts.getRelatorio(data_inicio, data_fim)
print(response)

```



## Licença

MIT
