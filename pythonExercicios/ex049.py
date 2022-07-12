num = int(input('Digite um número inteiro: '))
print(f'A tabuada no número {num} é:')
for c in range(1, 11):
    total = num * c
    print(f'{num} x {c} = {total}')
