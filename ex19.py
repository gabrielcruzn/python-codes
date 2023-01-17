def converta(hora, mmin):
    if 0 < hora <= 12 and 0 < min < 60:
        print(f'{hora}:{min} AM')
    elif 12 < hora < 24 and 0 < min < 60:
        print(f'{hora - 12}:{min} PM')
    else:
        print('Valor inválido')


while True:
    hora = int(input('Hora: '))
    if hora == 999: break
    min = int(input('Minuto: '))
    converta(hora,min)
    print('='*12)