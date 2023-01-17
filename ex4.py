print('***Operações numéricas***')
print()
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

opção = int(input('Escolha uma opção: '))

if opção == 1:
    print('\n**soma**')
    número1 = float(input('Digite o primeiro número: '))
    número2 = float(input('digite o segundo número: '))
    print('soma = ',(número1+número2))

elif opção == 2:
    print('\n**subtração**')
    número1 = float(input('Digite o primeiro número: '))
    número2 = float(input('digite o segundo número: '))
    print('subtração = ',(número1-número2))

elif opção == 3:
    print('\n**multiplicação**')
    número1 = float(input('Digite o primeiro número: '))
    número2 = float(input('digite o segundo número: '))
    print('multiplicação = ',(número1*número2))

elif opção == 4:
    print('\n**divisão**')
    número1 = float(input('Digite o primeiro número: '))
    número2 = float(input('digite o segundo número: '))
    print('divisão = ',(número1/número2))

else:
    print('Opção inválida')
