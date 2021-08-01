#!/usr/bin/env python

import sys

while True:
  linha = sys.stdin.readline().strip()
  if linha == '0':
    break
  n = int(linha)
  entrada_vagoes = [i + 1 for i in range(n)]
  linha = sys.stdin.readline().strip()
  while linha != '0':
    saida_vagoes = list(map(int, linha.split()))
    condicao = True
    pilha = []
    entrada = 0
    saida = 0
    while saida < n:
      if entrada < n and entrada_vagoes[entrada] == saida_vagoes[saida]:
        entrada += 1
        saida += 1
      elif len(pilha) > 0 and pilha[-1] == saida_vagoes[saida]:
        pilha.pop()
        saida += 1
      else:
        if entrada < n:
          pilha.append(entrada_vagoes[entrada])
          entrada += 1
        else:
          condicao = False
          break
    sys.stdout.write("Yes\n" if condicao else "No\n")
    linha = input().strip()
  print()