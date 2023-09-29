# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se alguém ganhou
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Inicializar o tabuleiro vazio
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"
jogadas = 0

while True:
    exibir_tabuleiro(tabuleiro)
    print(f"Jogador {jogador_atual}, é a sua vez.")
    
    linha = int(input("Digite o número da linha (0, 1, 2): "))
    coluna = int(input("Digite o número da coluna (0, 1, 2): "))
    
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1
    else:
        print("Essa posição já está ocupada. Tente novamente.")
        continue
    
    if verificar_vencedor(tabuleiro, jogador_atual):
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!")
        break
    elif jogadas == 9:
        exibir_tabuleiro(tabuleiro)
        print("Empate!")
        break
    
    jogador_atual = "X" if jogador_atual == "O" else "O"
