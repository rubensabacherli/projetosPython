def ctof (celsius):
    return ((celsius * (9/5)) + 32)

def ctok (celsius):
    return celsius + 273.15

def ftoc (fahrenheit):
    return (fahrenheit - 32) * 5/9

def ftok (fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def ktoc (kelvin):
    return kelvin - 273.15

def ktof (kelvin):
    return (kelvin - 273.15) * 9/5 + 32

print("Selecione a unidade de temperatura de entrada:\n[1] - Celsius\n[2] - Fahrenheit\n[3] - Kelvin")

entrada = int(input('Opção: '))
temperatura = float(input('Digite a temperatura a ser convertida: '))

print("Selecione a unidade de temperatura de saída:\n[1] - Celsius\n[2] - Fahrenheit\n[3] - Kelvin")

saida = int(input("Opção: "))

if entrada == 1:
    if saida == 1:
        resultado = temperatura
    elif saida == 2:
        resultado = ctof(temperatura)
    elif saida == 3:
        resultado = ctok(temperatura)
    else:
        print('Opções inválidas')
        
if entrada == 2:
    if saida == 2:
        resultado = temperatura
    elif saida == 1:
        resultado = ftoc(temperatura)
    elif saida == 3:
        resultado = ftok(temperatura)
    else:
        print('Opções inválidas')
        
if entrada == 3:
    if saida == 3:
        resultado = temperatura
    elif saida == 1:
        resultado = ktoc(temperatura)
    elif saida == 2:
        resultado = ktof(temperatura)
    else:
        print('Opções inválidas')
else:
    print('Opções inválidas')
    
print(f'{temperatura} -> {resultado:,.4f}')