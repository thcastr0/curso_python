#operadores de comparaçao e condicionais
primeiro_valor = input("digite o primeiro valor: ")
segundo_valor = input("digite o segundo valor: ")


if primeiro_valor > segundo_valor:
    print(primeiro_valor, 'é maior que o' , segundo_valor)

elif segundo_valor > primeiro_valor:
    print(segundo_valor, 'é maior que o' , primeiro_valor)

else:
    print('eles sao iguais')