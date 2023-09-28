from random import choice
import string

tamanhoSenha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''

for i in range(tamanhoSenha):
  senha += choice(caracteres) #seleciona um item da lista que foi criada com a biblioteca string.

print("A senha gerada é: ",senha)