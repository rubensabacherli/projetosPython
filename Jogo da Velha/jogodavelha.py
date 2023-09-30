import os
import random

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))
    
def jogador():
    global jogadas
    global quemJoga
    global maxJogadas
    
    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha: "))
        c = int(input("Coluna: "))
        
        while velha [l][c] != " ":
            l = int(input("Linha: "))
            c = int(input("Coluna: "))  
                  
        try:
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print('Linha ou coluna inválida!') 

def cpu():
    global jogadas
    global quemJoga
    global maxJogadas
    
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
    
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1
          
def verificaVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X","O"]
    
    for s in simbolos:
        vitoria = "n"
        indiceL = indiceC = 0
        
        while indiceL < 3:
            soma = 0
            indiceC = 0
            while indiceC < 3:
                if(velha[indiceL][indiceC] == s):
                    soma += 1
                indiceC += 1
            
            if(soma == 3):
                vitoria = "s"
                break
            indiceL += 1
            
        if(vitoria != "n"):
            break
        
        indiceL = indiceC = 0
        
        while indiceC < 3:
            soma = 0
            indiceL = 0
            while indiceL < 3:
                if(velha[indiceL][indiceC] == s):
                    soma += 1
                indiceL += 1
            
            if(soma == 3):
                vitoria = "s"
                break
            indiceC += 1
            
        if(vitoria != "n"):
            break
        
        soma = 0
        iDiagonal = 0
        while iDiagonal < 3:
            if(velha [iDiagonal][iDiagonal] == s):
                soma += 1
            iDiagonal += 1
            
        if (soma == 3):
            vitoria = s
            break
        
        soma = 0
        iDiagonalLinha = 0
        iDiagonalColuna = 2
        while iDiagonalColuna >= 0:
            if(velha [iDiagonalLinha][iDiagonalColuna] == s):
                soma += 1
            iDiagonalLinha += 1
            iDiagonalColuna -= 1
            
        if (soma == 3):
            vitoria = s
            break
        
    return vitoria  
 
def redefinir():
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    global velha
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"
    velha = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

while True:
    tela()
    jogador()
    cpu()
    tela()
    
    vit = verificaVitoria()
    
    if (vit != "n") or (jogadas >= maxJogadas):
        break