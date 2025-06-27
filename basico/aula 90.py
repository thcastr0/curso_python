"""
faça uma lista de compras com listas 

o usuario deve ter a posibilidade de inserir apagar e listarar valores da sua lista

nao permita que o programa quebre com erros de indice inexistentes na lista

"""

lista_compras = [ ]

comando = input('digite o que voce deseja fazer: adicinar, remover, listar ')

if comando == 'adicionar' or 'remover':
    item_comando = input('digite o item:')

    if comando == 'adicionar':
        lista_compras.append(item_comando)
    elif comando == 'remover':
        lista_compras.pop(item_comando)

elif comando == 'listar':
    print (lista_compras.enumere)
