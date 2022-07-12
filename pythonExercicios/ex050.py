s = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        s = s + num
print(f'O somatório dos números que são pares é: {s}')
