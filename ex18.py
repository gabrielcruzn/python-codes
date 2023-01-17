def valorPagamento(val,dia ):
    return val*1.03 + 0.001*dia

c = t = 0

while True:
    val = float(input('Valor da prestação: '))
    if val == 0:
        print(f'Total: {t}. Quantidade: {c} ')
        break
    dia = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: {valorPagamento(val, dia) :.2f}')
    print('-+-'*10)
    c += 1
    t += valorPagamento(val, dia)