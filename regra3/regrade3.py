a = b = c = 0

print('A está para B, assim como C está para X')

a = int(input('Digite A: '))
b = int(input('Digite B: '))
c = int(input('Digite C: '))

x = c * b
x = x / a

print(f'{a} está para {b}, assim como {c} está para {x:.2f}')