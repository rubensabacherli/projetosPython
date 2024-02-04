import random

print("Escolha sua jogada")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
print(" ")

jogador = int(input("Sua jogada: "))
if jogador == 1:
    print("Você escolheu Pedra!")
elif jogador == 2:
    print("Você escolheu Papel!")
elif jogador == 3:
    print("Você escolheu Tesoura!")

print(" ")

pc = random.randint(1,3)
if pc == 1:
    print("O Computador escolheu Pedra!")
elif pc == 2:
    print("O Computador escolheu Papel!")
elif pc == 3:
    print("O Computador escolheu Tesoura!")

print(" ")

if  jogador == pc:
    print("Empate!")
elif jogador == 1 and pc == 3:
    print("Você ganhou!") 
elif jogador == 2 and pc == 1:
    print("Você ganhou!") 
elif jogador == 3 and pc == 2:
    print("Você ganhou!") 
else:
    print("O computador ganhou!")