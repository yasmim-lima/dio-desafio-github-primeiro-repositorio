nome = input('Digite seu nome completo: ').strip()
print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
qtd_total = len(nome) - nome.count(' ')
print(f'Quantidade de letras ao todo: {qtd_total}')
nome = nome.split()
print(f'Quantidade de letras que o primeiro nome possui: {len(nome[0])}')





