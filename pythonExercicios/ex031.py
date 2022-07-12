distancia = float(input('Qual a distância em Km/h da viagem? '))
if distancia <= 200:
    passagem = 0.50 * distancia
    print(f'O preço da passagem para essa viagem é R${passagem:.2f}.')
else:
    passagem = 0.45 * distancia
    print(f'O preço da passagem para essa viagem é R${passagem:.2f}.')


