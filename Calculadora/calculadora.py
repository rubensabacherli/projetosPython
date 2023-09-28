operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')

while True:
    
    if operacao == '5':
        print('Até mais!')
        break
    elif operacao in ('1', '2', '3', '4'):
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if operacao == '1':
            res = num1 + num2
            print(f'Resultado: {res}')
            operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')
        elif operacao == '2':
            res = num1 - num2
            print(f'Resultado: {res}')
            operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')
        elif operacao == '3':
            res = num1 * num2
            print(f'Resultado: {res}')
            operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')
        elif operacao == '4':
            if num2 == 0:
                print('Não é possível dividir por zero.')
                operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')
            else:
                res = num1 / num2
                print(f'Resultado: {res}')
                operacao = input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair\nSelecione o número correspondente a Operação: ')
    else:
        print('Opção inválida. Tente novamente')
