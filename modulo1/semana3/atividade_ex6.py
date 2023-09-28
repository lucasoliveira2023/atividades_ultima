def gorjeta(valor, porcentagem):
  #Comece seu código aqui
  gorjeta = valor * porcentagem / 100
  return gorjeta

valor_conta = float(input())
porcentagem = int(input())
resultado = gorjeta(valor_conta, porcentagem)
print(f"{resultado:.2f}")