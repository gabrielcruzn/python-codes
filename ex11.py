from random import randint
from time import sleep

computador = randint(1, 5) #Faz o computador sortear um número

print('-=-' * 20)
print('Será sorteado um número de 1 a 5, tende adivinhar...')
print('-=-' * 20)

jogador = int(input('Chute o número sorteado: '))

print('PROCESSANDO...')
sleep(1.5)

if jogador == computador:
    print(f'Você acertou, o número sorteado foi mesmo o {computador}')

elif jogador > 5:
    print('OPÇÃO INVÁLIDA, O SORTEIO É DE 1 A 5 SEU ARROMBADO')

else:
    print(f'Você errou, o número sorteado foi {computador} e não {jogador}')