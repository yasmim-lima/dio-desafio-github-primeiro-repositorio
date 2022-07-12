from math import trunc
num = int(input('Digite um número entre 0 e 9999: '))
unidade = num % 10
dezena = (num % 100) * 0.1
centena = (num % 1000) * 0.01
milhar = (num % 10000) * 0.001
print(f'unidade: {unidade}')
print(f'dezena: {trunc(dezena)}')
print(f'centena: {trunc(centena)}')
print(f'milhar: {trunc(milhar)}')

