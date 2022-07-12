s = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c
print(f'A soma entre todos os números ímpares que são mútiplos de três e que se encontram no intervalo de 1 até 500 é {s}')

