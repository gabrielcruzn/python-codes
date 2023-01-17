from datetime import date
atual = date.today().year
for pessoas in range(1,5):
    nascimento =  int(input('Qual o ano de nascimento da pessoa? '))
    idade = atual - nascimento


    if idade >= 18:
        print(f'Essa pessoa tem {idade} e é maior de idade.')

    elif idade >= 60:
        print(f'Essa pessoa tem {idade} e é idosa')

    else:
        print(f'Essa pessoa tem {idade} e é menor de idade.')