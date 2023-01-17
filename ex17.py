def CPF(temperatura):
    return 1.8*temperatura+32;

def FPC(temperatura):
    return (temperatura-32)/1.8;

def CPK(temperatura):
    return (temperatura+273);

def KPC(temperatura):
    return (temperatura-273);


def main():
    print("Conversor de temperatura")
    #aqui dentro você chama as outras funções criadas

    print("Escolha uma converção: ");
    print("1 - Celsius para Fahrenheit ");
    print("2 - Fahrenheit para Celsius");
    print("3 - Celsius para Kelvin");
    print("4 - Kelvin para Celsius");
    print("5 - Sair")
    opcao = int(input());

    temperaturatual = int(input("Digite a temperatura atual:"));

    if(opcao == 1):
        print ((1.8*temperaturatual+32),"esta é sua temperatura em Fahrenheit");
    elif(opcao == 2):
        print ((temperaturatual-32)/(18/10),"esta é sua temperatura em Celsius");
    elif(opcao == 3):
        print ((temperaturatual+273),"esta é sua temperatura em Kelvin");
    elif(opcao == 4):
        print ((temperaturatual-273),"esta é sua temperatura em Celsius");
    else:
        print("Opção invalida")

if __name__ == '__main__':
    main()