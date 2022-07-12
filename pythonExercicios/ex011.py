altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print(f'A área da parede é {area:.1f} metros quadrados e para para pintá-la será necessário {tinta:.1f}L de tinta')
