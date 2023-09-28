def conta_letras(letra_buscada, frase):
  contagem = 0 #Inicia a contagem a partir do zero
  #Escreva o seu código a partir daqui
  for letra in frase:
      if letra == letra_buscada:
          contagem += 1
  return contagem

letra = input()
frase = input()
saida = conta_letras(letra, frase)
print(saida)