#!/usr/bin/env python
from cliente import Cliente
from chamada import Chamada

cliente = Cliente('token', 'host');
chamada = Chamada(cliente)
r = chamada.getChamada("ID")
print r