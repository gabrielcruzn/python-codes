def mostra_resultado(area, salario, projecao, salario_final):
    print(f"""O funcionário de perfil de {area},tem salário inicial de {salario}, e após {projecao} anos seu salário será de {salario_final} reais.""")


def operador(anos):
    salario_base = 1500
    aumento = 1.2
    salario = 0
    salario = salario_base

    qtd_aumento = int(anos // 4)
    print(qtd_aumento)

    if qtd_aumento == 0:
        return salario_base

    for i in range(0, qtd_aumento):
        salario = salario * aumento

    return mostra_resultado("Operador", salario_base, anos, salario)


def tecnico(anos):
    salario_base = 2500
    aumento = 1.15
    salario = 0
    salario = salario_base

    qtd_aumento = int(anos // 3)
    print(qtd_aumento)

    if qtd_aumento == 0:
        return salario_base

    for i in range(0, qtd_aumento):
        salario = salario * aumento

    return mostra_resultado("Técnico", salario_base, anos, salario)


def gerente(anos):
    salario_base = 4500
    aumento = 1.1
    salario = 0
    salario = salario_base

    qtd_aumento = int(anos // 2)
    print(qtd_aumento)

    if qtd_aumento == 0:
        return salario_base

    for i in range(0, qtd_aumento):
        salario = salario * aumento

    return mostra_resultado("Gerente", salario_base, anos, salario)


def main():
    tipo = int(input("""Qual seu perfil?
    1- Operador
    2- Técnico
    3- Gerente"""))

    proj_anos = int(
        input("Qual o tempo de projeção do seu salário?"))

    if tipo == 1:
        operador(proj_anos)
    elif tipo == 2:
        tecnico(proj_anos)
    elif tipo == 3:
        gerente(proj_anos)


main()