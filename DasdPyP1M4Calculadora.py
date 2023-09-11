#Fazer uma calculadora que realize as operações soma, subtração, Multiplicação, Divisão e Exponenciação e pergunte se quer continuar
while True:
    print('a : Soma\nb : Multiplicação\nc : Subtração\nd : Divisão\ne : Exponenciação\n\n')
    while True:
        opção = str(input('Sua opção: ')).upper().strip()[0]
        if opção not in 'ABCDE':
            print('\033[31;1mERRO DIGITE UM VALOR VÁLIDO!\033[m')
        else:
            break
    if opção in 'A':
        n1 = int(input('1ºNúmero: '))
        n2 = int(input('2ºNúmero: '))
        print(f'{n1+n2}')
    elif opção in 'B':
        n1 = int(input('1ºNúmero: '))
        n2 = int(input('2ºNúmero: '))
        print(f'{n1*n2}')
    elif opção in 'C':
        n1 = int(input('1ºNúmero: '))
        n2 = int(input('2ºNúmero: '))
        print(f'{n1-n2}')
    elif opção in 'D':
        n1 = int(input('1ºNúmero: '))
        n2 = int(input('2ºNúmero: '))
        print(f'{n1/n2}')
    else:
        n1 = int(input('1ºNúmero: '))
        n2 = int(input('Elevado a:  '))
        print(f'{n1**n2}')
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('\033[0;31;1mERRO DIGITE UM VALOR VÁLIDO!\033[m')
    