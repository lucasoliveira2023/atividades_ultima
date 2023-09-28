def verifica_prefixo(palavra1, palavra2):
  tamanho = len(palavra1)
  for indice in range(tamanho):
    if palavra1[indice] != palavra2[indice]:
      return False
  return True

palavra1 = input()
palavra2 = input()
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)