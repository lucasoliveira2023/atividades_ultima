def positivo_negativo_zero(numero):
  #Comece seu código aqui
  if numero > 0:
      return "Positivo"
  elif numero < 0:
      return "Negativo"
  else:
      return "Zero"

numero = int(input())
print(positivo_negativo_zero(numero))