cidade = input('Digite o nome de uma cidade: ').strip().upper()
lista = cidade.split()
palavra = 'SANTO' in lista[0]
print(f'A cidade começa com a palavra SANTO?\n{palavra}')

