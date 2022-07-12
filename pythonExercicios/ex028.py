from random import randint
computador = randint(0, 5)
print('Vou escolher o número de 0 a 5.....')
num = int(input('Adivinhe o número que eu escolhi: '))
if num == computador:
    print('Acertou! Você ganhou!')
