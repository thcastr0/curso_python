"""
faça um jogo para adivinhar qual a palavra secreta 


- voce propoem uma palavra secreta, dando oprtunidade de o usuario escrever uma letra
se ele acertar voce mostra a letra, se errar mostre *

faça contagem de tentativas 

"""

palavra_secreta = 'casa'
letras_acertadas = ''
tentativas = 0

while True:
    letra_usuario = input('qual a letra ? ')
    tentativas = tentativas + 1 
    if len(letra_usuario) > 1:
        print('digite apenas 1 letra')
        continue
    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario 
   
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print('voce ja acertou: ',palavra_formada)
    if palavra_formada == palavra_secreta:
        print(f'voce ganhou, a palavra secreta era {palavra_secreta} e voce teve {tentativas} tentativas')
        letras_acertadas = ''
        tentativas = 0