#!/usr/bin/env python

import sys

validos = {
  "A":"A", "B":"", "C":"", "D":"", "E":"3",
  "F":"", "G":"", "H":"H", "I":"I", "J":"L",
  "K":"", "L":"J", "M":"M", "N":"", "O":"O",
  "P":"", "Q":"", "R":"", "S":"2", "T":"T",
  "U":"U", "V":"V", "X":"X", "W":"W", "Y":"Y",
  "Z":"5", "1":"1", "2":"S", "3":"E", "4":"",
  "5":"Z", "6":"", "7":"", "8":"8", "9":""
}

linhas = list(map(str.strip, sys.stdin.readlines()))

for palavra in linhas:
  tamanho_palavra = len(palavra)
  palindromo = True
  espelhado = True

  for indice in range(int(tamanho_palavra / 2 + 1)):
    if palavra[indice] != palavra[tamanho_palavra - indice - 1]:
      palindromo = False
      break

  for indice in range(int(tamanho_palavra / 2 + 1)):
    if validos[palavra[indice]] != palavra[tamanho_palavra - indice - 1]:
      espelhado = False
      break

  if palindromo and espelhado:
    print("{palavra} -- is a mirrored palindrome.\n".format(palavra=palavra))
  elif not palindromo and espelhado:
    print("{palavra} -- is a mirrored string.\n".format(palavra=palavra))
  elif palindromo and not espelhado:
    print("{palavra} -- is a regular palindrome.\n".format(palavra=palavra))
  elif not palindromo and not espelhado:
    print("{palavra} -- is not a palindrome.\n".format(palavra=palavra))