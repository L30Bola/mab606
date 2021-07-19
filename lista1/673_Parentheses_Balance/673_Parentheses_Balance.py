#!/usr/bin/env python

import sys

linhas = int(sys.stdin.readline().strip())
resultados = []

for linha in range(linhas):
  parenteses = 0
  colchetes = 0
  invalido = False
  letra_anterior = False

  texto = sys.stdin.readline().strip()

  if len(texto) == 0:
    resultados.append("Yes")
    continue

  for letra in texto:
    if letra in ("]",")") and parenteses == 0 and colchetes == 0:
      resultados.append("No")
      invalido = True
      break

    if letra_anterior:
      if (letra == "]" and letra_anterior == "(") or (letra == ")" and letra_anterior == "["):
        resultados.append("No")
        invalido = True
        break

    if letra == "[":
      colchetes += 1
    elif letra == "(":
      parenteses += 1
    elif letra == "]":
      colchetes -= 1
    elif letra == ")":
      parenteses -= 1
    letra_anterior = letra

    if parenteses < 0 or colchetes < 0:
      resultados.append("No")
      invalido = True
      break

  if not invalido:
    if colchetes != 0 or parenteses != 0:
      resultados.append("No")
    else:
      resultados.append("Yes")

for resultado in resultados:
  print(resultado)
