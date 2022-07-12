frase = input('Digite uma frase: ').strip().upper()
lista = list(frase)
qtd = frase.count('A')
print(f'A letra "A" aparece {qtd} vez(es)')
posicao1 = frase.find('A') + 1
print(f'Ela aparece pela primeira vez na posição {posicao1}')
ultima = frase.rfind('A') + 1
print(f'Ela aparece pela última vez na posição {ultima}')
