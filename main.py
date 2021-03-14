from random import randint, sample
import time
print('\033[0;33m{:=^44}'.format('\033[0;33m LOTERIAS '))
print(''' 
[1] = QUINA
[2] = MEGA SENA
[3] = DUPLA SENA
[4] = LOTOFÁCIL
[5] = lOTOMANIA
[6] = DIA DE SORTE''')
loto = int(input('Escolha sua loteria: '))
while loto > 6 or loto < 1:
  loto = int(input('\033[0;34mEntre com uma opção válida: '))
if loto == 1:
  opção, init, fim, qdezInit, qdezFim = ' QUINA', 0, 80, 5, 15
elif loto == 2:
    opção, init, fim, qdezInit, qdezFim  = 'MEGA SENA', 1, 60, 6, 15
elif loto == 3:
    opção, init, fim, qdezInit, qdezFim = 'DUPLA SENA', 1, 50, 6, 15
elif loto == 4:
    opção, init, fim, qdezInit, qdezFim = 'LOTOFÁCIL', 1, 25, 15, 20
elif loto == 5:
    opção, init, fim, qdezInit, qdezFim  = 'lOTOMANIA', 0, 99, 50, 50
elif loto == 6:
    opção, init, fim, qdezInit, qdezFim  = 'DIA DE SORTE', 1, 30, 7, 15
    Mes =  sample(range(1, 12), 1)
print('Você escolheu {}, Ótima escolha!'.format(opção))
qdezenas = int(input('\033[0;33mEscolha um jogo entre {} e {} Dezenas\033[0;33m: '.format(qdezInit, qdezFim)))
while qdezenas < qdezInit or qdezenas > qdezFim:
    qdezenas = int(input('Entre com uma opção valida: '))
print('-='*27)
print('Muito bem! Você escolheu a {} com {} Dezenas!'.format(opção, qdezenas))
print('-='*27)
print('\033[0;34m-='*50)
print('\033[0;33mSorteando os Números...')
time.sleep(1)
dezenas = sorted(sample(range(init, fim),qdezenas))
print('\033[0;34mAqui {} Dezenas da Sorte: {}'.format(qdezenas ,dezenas))
print('O Mês escolhido foi: {} '.format(Mes) if loto == 6 else '-='*50)
print('-='*50 if loto == 6 else '')


