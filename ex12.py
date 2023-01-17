veloecidad = float(input('Qual é a velocidade atual do carro? '))
if veloecidad > 80:
    print('VOCê FOI MULTADO! O limite de 80km/h foi excedido.')
    print(f'Sua multa é de {(veloecidad-80)*7}')
else:
    print('Continue dirigindo com segurança, tenha uma boa viagem!')