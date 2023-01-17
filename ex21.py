from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de sortear um número de 0 a 10!')
print('Voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1

    if jogador == computador:
        acertou = True
print(f'ACERTOU! Com apenas {palpites}')

