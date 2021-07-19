#!/usr/bin/env python

import sys

def formacao(coluna, linha):
  if coluna < linha:
    return formacao(linha, coluna)
  elif linha == 1:
    return coluna
  elif linha == 2:
    if coluna % 4 > 1:
      resto = 2
    else:
      resto = coluna % 4
    return 4 * int(coluna / 4) + resto * 2
  else:
    return int((coluna * linha + 1) / 2)

entrada = list(map(str.split, sys.stdin.readlines()))
for valores in entrada:
  if int(valores[0]) == 0 and int(valores[1]) == 0:
    break

  print("{cavalos} knights may be placed on a {linha} row {coluna} column board.".format(
      cavalos=formacao(int(valores[0]), int(valores[1])), linha=valores[0], coluna=valores[1]
  ))
