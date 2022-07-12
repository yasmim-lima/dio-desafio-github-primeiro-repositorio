lista_animais = list()


def validar_inteiro(aux_numero):
  valido = True
  try:
    aux_numero = int(aux_numero)
  except:
    valido = False
    print('O código digitado é inválido, tente novamente.')
  return valido


def validar_string(aux_texto):
  valido = True
  try:
    aux_texto = float(aux_texto)
    valido = False
  except:
    print('O texto informado é um número, digite novamente.')
  return valido


def cadastrar_animal(cod_animal, nome_animal, sexo_animal, idade_animal, raca_animal, nome_dono, tel_dono):
  cadastrou = False
  cod_animal = int(cod_animal)
  nome_animal = str(nome_animal)
  sexo_animal = str(sexo_animal)
  idade_animal = str(idade_animal)
  raca_animal = str(raca_animal)
  nome_dono = str(nome_dono)
  tel_dono = int(tel_dono)
  if existe_cadastro(cod_animal) == False:
    aux_animal = dict()
    aux_animal['Código'] = cod_animal
    aux_animal['Nome'] = nome_animal
    aux_animal['Sexo'] = sexo_animal
    aux_animal['Idade'] = idade_animal
    aux_animal['Raça'] = raca_animal
    aux_animal['Responsável'] = nome_dono
    aux_animal['Telefone'] = tel_dono
    lista_animais.append(aux_animal.copy())
    aux_animal.clear()
    cadastrou = True

  if(cadastrou):
    print("Animal cadastrado com sucesso!")
  else:
    print("\nJá existe um animal cadastrado com esse código.")
  return cadastrou


def existe_cadastro(cod_animal):
  existe = False
  for animal in lista_animais:
    if animal['Código'] == cod_animal:
      existe = True
      break
  return existe


def atualizar_animal(aux_cod_animal, aux_tel_dono, aux_idade_animal):
  atualizou = False
  for animal in lista_animais:
    if animal['Código'] == aux_cod_animal:
      animal['Telefone'] = aux_tel_dono
      atualizou = True
      break
    if animal['Código'] == aux_cod_animal:
      animal['Idade'] = aux_idade_animal
      atualizou = True
      break
  return atualizou


def remover_animal(aux_cod_animal):
  removeu = False
  for animal in lista_animais:
    if animal['Código'] == aux_cod_animal:
      lista_animais.remove(animal)
      removeu = True
      break
  return removeu


def pesquisar_animal(cod_animal):
  aux_animal = dict()
  for animal in lista_animais:
    if animal['Código'] == cod_animal:
      aux_animal = animal
      break
  return aux_animal


def imprimir_animais():
  print("Imprimindo a lista de animais cadastrados:\n")
  print("{:<10} {:<18} {:<10} {:<15} {:<25} {:<20} {:<8} ".format("CÓDIGO", "NOME", "SEXO", "IDADE", "RAÇA", "RESPONSÁVEL", "TELEFONE"))
  for animal in lista_animais:
    print("{:<10} {:<18} {:<10} {:<15} {:<25} {:<20} {:<8}".format(animal['Código'], animal['Nome'], animal['Sexo'], animal['Idade'], animal['Raça'], animal['Responsável'], animal['Telefone']))


def imprimir_um_animal(aux_animal):
  print("{:<10} {:<18} {:<10} {:<15} {:<25} {:<20} {:<8} ".format("CÓDIGO", "NOME", "SEXO", "IDADE", "RAÇA", "RESPONSÁVEL", "TELEFONE"))
  print("{:<10} {:<18} {:<10} {:<15} {:<25} {:<20} {:<8}".format(aux_animal['Código'], aux_animal['Nome'], aux_animal['Sexo'], aux_animal['Idade'], aux_animal['Raça'], aux_animal['Responsável'], aux_animal['Telefone']))


print('-'*50)
print('         ANIMAIS AJU CLÍNICA VETERINÁRIA')
print('-'*50)
cadastrar_animal(1, 'Belinha', 'Fêmea', '10 anos', 'Shih Tzu', 'Márcia Silva', 87549902)
cadastrar_animal(2, 'Zeca', 'Macho', '2 meses', 'Siamês', 'Yuri Cardoso', 69542381)
cadastrar_animal(3, 'Jujuba', 'Fêmea', '5 anos', 'Poodle', 'Marcela Araújo', 87549902)

print('-'*50)
print('Lista de veterinários disponíveis para realizar a consulta:')
print('1 - Dr. Thiago Mota')
print('2 - Dra. Vanessa Santos')
print('3 - Dr. Pedro Henrique')
op = int(input('Escolha uma das opções acima: '))
if op == 1:
  print('CONSULTA COM DR. THIAGO MOTA: ')
  for i in range(1):
    cod_animal = int(input("Informe o código do animal que deseja pesquisar: "))
    if existe_cadastro(cod_animal):
      print("O animal pesquisado é: ")
      imprimir_um_animal(pesquisar_animal(cod_animal))
    else:
      print("O animal pesquisado não existe na base de dados!")
      for i in range(1):
        codigo = input('Digite o código: ')
        while True:
          if validar_inteiro(codigo):
            nome = str(input('Digite o nome do pet: '))
            sexo = str(input('Digite o sexo do pet: '))
            idade = str(input('Digite a idade do pet: '))
            raca = str(input('Digite a raça do pet: '))
            dono = str(input('Digite o nome do responsável:'))
            tel = int(input('Digite o telefone para contato (sem o hífen): '))
            cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
            break
          else:
            codigo = str(input('Digite o código:'))
            if validar_inteiro(codigo):
              nome = str(input('Digite o nome do pet: '))
              sexo = str(input('Digite o sexo do pet: '))
              idade = str(input('Digite a idade do pet: '))
              raca = str(input('Digite a raça do pet: '))
              dono = str(input('Digite o nome do responsável:'))
              tel = int(input('Digite o telefone para contato (sem o hífen): '))
              cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
              break
            else:
              continue
  receita = input('Digite o que o foi receitado: ')
  print('-'*50)
  print(f'RECEITUÁRIO: {receita}')

elif op == 2:
    print('CONSULTA COM DRA. VANESSA SANTOS: ')
    for i in range(1):
      cod_animal = int(input("Informe o código do animal que deseja pesquisar: "))
      if existe_cadastro(cod_animal):
        print("O animal pesquisado é: ")
        imprimir_um_animal(pesquisar_animal(cod_animal))
      else:
        print("O animal pesquisado não existe na base de dados!")
        for i in range(1):
          codigo = input('Digite o código: ')
          while True:
            if validar_inteiro(codigo):
              nome = str(input('Digite o nome do pet: '))
              sexo = str(input('Digite o sexo do pet: '))
              idade = str(input('Digite a idade do pet: '))
              raca = str(input('Digite a raça do pet: '))
              dono = str(input('Digite o nome do responsável:'))
              tel = int(input('Digite o telefone para contato (sem o hífen): '))
              cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
              break
            else:
              codigo = str(input('Digite o código:'))
              if validar_inteiro(codigo):
                nome = str(input('Digite o nome do pet: '))
                sexo = str(input('Digite o sexo do pet: '))
                idade = str(input('Digite a idade do pet: '))
                raca = str(input('Digite a raça do pet: '))
                dono = str(input('Digite o nome do responsável:'))
                tel = int(input('Digite o telefone para contato (sem o hífen): '))
                cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
                break
              else:
                continue
    receita = input('Digite o que o foi receitado: ')
    print('-'*50)
    print(f'RECEITUÁRIO: {receita}')

elif op == 3:
  print('CONSULTA COM DR. PEDRO HENRIQUE: ')
  for i in range(1):
    cod_animal = int(input("Informe o código do animal que deseja pesquisar: "))
    if existe_cadastro(cod_animal):
      print("O animal pesquisado é: ")
      imprimir_um_animal(pesquisar_animal(cod_animal))
    else:
      print("O animal pesquisado não existe na base de dados!")
      for i in range(1):
        codigo = input('Digite o código: ')
        while True:
          if validar_inteiro(codigo):
            nome = str(input('Digite o nome do pet: '))
            sexo = str(input('Digite o sexo do pet: '))
            idade = str(input('Digite a idade do pet: '))
            raca = str(input('Digite a raça do pet: '))
            dono = str(input('Digite o nome do responsável:'))
            tel = int(input('Digite o telefone para contato (sem o hífen): '))
            cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
            break
          else:
            codigo = str(input('Digite o código:'))
            if validar_inteiro(codigo):
              nome = str(input('Digite o nome do pet: '))
              sexo = str(input('Digite o sexo do pet: '))
              idade = str(input('Digite a idade do pet: '))
              raca = str(input('Digite a raça do pet: '))
              dono = str(input('Digite o nome do responsável:'))
              tel = int(input('Digite o telefone para contato (sem o hífen): '))
              cadastrar_animal(codigo, nome, sexo, idade, raca, dono, tel)
              break
            else:
              continue
  receita = input('Digite o que o foi receitado: ')
  print('-'*50)
  print(f'RECEITUÁRIO: {receita}')

print('-'*50)
imprimir_animais()
print('-'*50)
cod_animal = int(input('Informe o código do animal que deseja remover: '))
remover_animal(cod_animal)
imprimir_animais()
print('-'*50)
cod_animal_atualizar = str(input('Informe o código do animal que deseja atualizar: '))
idade_animal = str(input('Informe a idade atual do animal: '))
tel_dono = int(input('Informe o número de telefone atual do responsável: '))
atualizar_animal(tel_dono, idade_animal, cod_animal_atualizar)
imprimir_animais()













