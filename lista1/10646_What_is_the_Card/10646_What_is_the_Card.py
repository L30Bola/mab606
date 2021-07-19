#!/usr/bin/env python

import sys

def definir_valor_carta(carta):
  if carta[0] in ("T","J","Q","K","A"):
    return 10
  else:
    return int(carta[0])

linhas = int(sys.stdin.readline().strip())
rodadas = 3

for linha in range(linhas):
  texto = sys.stdin.readline().strip()
  cartas = texto.split()
  mao_inicial = cartas[27:52]
  deck = cartas[:27]
  Y = 0
  for rodada in range(rodadas):
    tamanho_deck = len(deck)
    X = definir_valor_carta(deck[-1])
    cartas_removidas = 10 - X + 1
    deck = deck[:tamanho_deck - cartas_removidas]
    Y += X
  cartas = deck + mao_inicial
  print("Case {rodada}: {carta}".format(
    rodada=linha+1, carta=cartas[Y-1]
  ))
