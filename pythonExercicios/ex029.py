velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade, que é 80Km/h, e terá que pagar R${multa:.2f} de multa.')
else:
    print('Você está dentro do limite de velocidade.')
