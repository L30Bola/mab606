#!/usr/bin/env python

import sys
import collections

listas = list(map(str.split, sys.stdin.readlines()))
entrada = [item for sublist in listas for item in sublist] # simplificando as listas, para facilitar
contador = collections.Counter()
palavras = []

for palavra in entrada:
  if palavra == "#":
    break

  palavra_simplificada = "".join(sorted(palavra.lower()))
  if len(palavra) >= 1:
    contador[palavra_simplificada] += 1
  palavras.append((palavra, palavra_simplificada))

lista_auxiliar_palavras = []
for palavra, palavra_simplificada in palavras:
  if not palavra_simplificada in contador or contador[palavra_simplificada] < 2:
    lista_auxiliar_palavras.append(palavra)

for resultado in sorted(lista_auxiliar_palavras):
  print(resultado)