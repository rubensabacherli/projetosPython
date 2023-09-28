from palavraforca import palavras #Traz a variável do tipo lista que criei no outro arquivo python contendo palavras variadas, dessa forma quem estiver vendo o código, não verá as palavras especificadas.
import random

#Declaração de variáveis.
palavra = random.choice(palavras)
letras_usuario = []
chances = 6
ganhou = False

while True:
    for letra in palavra:
        
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
            
    print('\n')
            
    if chances == 6:
        print('____')
        print('|  |')
        print('|')
        print('|')
        print('|')
    elif chances == 5:
        print('____')
        print('|  |')
        print('|  O')
        print('|')
        print('|')
    elif chances == 4:
        print('____')
        print('|  |')
        print('|  O')
        print('|  |')
        print('|')
    elif chances == 3:
        print('____')
        print('|  |')
        print('|  O')
        print('|  |')
        print('|  /')
        print('|')
    elif chances == 2:
        print('____')
        print('|  |')
        print('|  O')
        print('|  |')
        print('|  Λ')
        print('|')
    elif chances == 1:
        print('____')
        print('|  |')
        print('|  O')
        print('|  |-')
        print('|  Λ')
        print('| ')

            
    tentativa = input('Digite uma letra: ')
    letras_usuario.append(tentativa.lower())
        
    if tentativa.lower() not in palavra.lower():
        chances -= 1
        
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
    
        
    if chances == 0 or ganhou:
        break
    
if ganhou:
    print(f"Parabens, você ganhou! A palavra era: {palavra}")
else:
    print('____')
    print('|  |')
    print('|  O')
    print('| -|-')
    print('|  Λ')
    print('|')
    print(f"Você Perdeu! A palavra era: {palavra}")
