#exercicio de jokenpo
from random import randint
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
#gerador de numero aleatório entre 0 e 2
comp = randint(0 , 2)
print('''Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Digite uma opção: '))
#criar interatividade no jogo com o sleep
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('=-' *13)
print('O computador jogou {}' .format(lista[comp]))
print('O jogador jogou {}' .format(lista[jogador]))
print('=-' *13)
#testanto as condições
if comp == 0: #computador jogou pedra
    if jogador == 0:
        print('Empatou!!')
    elif jogador ==1:
        print('Jogador Perdeu!')
    elif jogador ==2:
        print('Jogador Ganhou!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1: #computador jogou papel
    if jogador == 0:
        print('Jogador Perdeu!')
    elif jogador == 1:
        print('Empatou!!')
    elif jogador == 2:
        print('Jogador Ganhou!')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador Ganhou!')
    elif jogador == 1:
        print('Jogador Perdeu!')
    elif jogador == 2:
        print('Empatou!!')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA!')
