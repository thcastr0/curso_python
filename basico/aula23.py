#exercicios variaveis e tipos de dados 
nome=input("qual o seu nome ? ")
sobrenome=input("qual o seu sobrenome ? ")
idade=input("qual sua idade ? ")

ano_nascimento= idade - 2025

if idade >= 18:
    maior_idade = "sim"
else:
   maior_idade = "não"

altura_metros= input("qual sua altura em metros? ")





print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('idade:', idade)
print('ano nascimento:', ano_nascimento)
print('é maior de idade:', maior_idade)
print('altura em metros:', altura_metros)
