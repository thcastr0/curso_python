"""
exercicio 1: faça um programa que peça ao ussuario para digitar um numero int e informar se é par ou impar, caso nao digite um nuemro int informar que nao é um numero inteiro 

"""
numero = (input('digite um numero inteiro: '))
try:
    if numero % 2 == 0:
        print(f'{numero} é um numero par')

    elif numero % 2 == 1:
        print(f'{numero} é um numero impar')
except:
    print(f'{numero} nao é um numero inteiro')


"""
exercicio 2:
programa que pergunte a hora e exiba uma saudação apropriada = bom dia 00-11, boa tarde 12 a 17, boa noite 18 a 23 

"""
hora = input('que horas são ? ')
try:
    hora_int = int(hora)
    if 0>= hora and hora <=11:
        print('bom dia')

    elif 11 > hora and hora <=17:
        print('bom dia')    

    elif 17> hora and hora <=23:
        print("boa noite")

except:
    print('nao é um numero')


