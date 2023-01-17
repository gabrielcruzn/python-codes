print('OPERAÇÕES NUMÉRICAS:')
print('-----------------')
print('1 - soma')
print('2 - subtração')
print('3 - divisão')
print('4 - multiplicação')
print('5 - potenciação')
print('6 - radiciação')
print('-----------------')

opção = int(input('Digite o número da operação que deseja: '))

if opção == 1:
    print('\n**SOMA**')
    n1 = float(input('Digite a primeira parcela: '))
    n2 = float(input('Digite a segunda parcela: '))
    print(f'Soma = {n1+n2}')

elif opção == 2:
    print('\n**SUBTRAÇÃO**')
    n1 = float(input('Digite o minuendo: '))
    n2 = float(input('Digite o subtraendo: '))
    print(f'Resto = {n1-n2}')

elif opção == 3:
    print('\n**DIVISÃO**')
    n1 = float(input('Digite o dividendo: '))
    n2 = float(input('Digite o divisor: '))
    print(f'Quociente = {n1/n2}')

elif opção == 4:
    print('\n**MULTIPLICAÇÃO**')
    n1 = float(input('Digite o primeiro fator: '))
    n2 = float(input('Digite o segundo fator: '))
    print(f'Produto = {n1*n2}')

elif opção == 5:
    print('\n**POTENCIAÇÃO**')
    n1 = float(input('Digite a base: '))
    n2 = float(input('Digite o expoente: '))
    print(f'Potência = {n1**n2}')

elif opção == 6:
    print('\n**RADICIAÇÃO**')
    n1 = float(input('Digite o radicando: '))
    n2 = float(input('Digite o indice: '))
    print((f'Raiz = {n1**(1/n2)}'))

else:
    print('OPÇÃO INVÁLIDA')
