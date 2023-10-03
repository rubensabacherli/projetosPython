import random

def adivinha(x):
    numero_aleatorio = random.randint(1, x)
    chute = 0
    while chute != numero_aleatorio:
        chute = int(input(f'Chute um número entre 1 e {x}: '))
        if chute < numero_aleatorio:
            print('Mais')
        elif chute > numero_aleatorio:
            print('Menos')
    
    print(f'Acertou! O número aleatório era {numero_aleatorio}.')        
    

def pcadivinha(x):
    baixo = 1
    alto = x
    retorno = ''

    while retorno != 'c':
        if baixo != alto:
            numero_aleatorio = random.randint(baixo, alto)
        else:
            numero_aleatorio = baixo
        retorno = input(f'{numero_aleatorio} Foi muito(M), pouco(P) ou está correto(C)? ').lower()
        if retorno == 'm':
            alto = numero_aleatorio - 1
        elif retorno == 'p': 
            baixo = numero_aleatorio + 1
    print(f'Correto! O Número era {numero_aleatorio}')

        

pcadivinha(10)