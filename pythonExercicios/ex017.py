from math import hypot
op = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa do triângulo é {hypot(op,adj):.2f}')
