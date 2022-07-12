dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
total = (60 * dias) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')
