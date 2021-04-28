from random import randint, sample,choice
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
    Meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    mesecolhido = choice(Meses) # escolhe um mês dentre os meses
print(f'Você escolheu {opção}, Ótima escolha!')
qdezenas = int(input(f'\033[0;33mEscolha um jogo entre {qdezInit} e {qdezFim} Dezenas\033[0;33m: '))
while qdezenas < qdezInit or qdezenas > qdezFim:
    qdezenas = int(input('Entre com uma opção valida: '))
print('-='*27)
print(f'Muito bem! Você escolheu  {opção} com {qdezenas} Dezenas!')
print('-='*27)
print('\033[0;34m-='*42)
print('\033[0;33mSorteando as Dezenas...')
time.sleep(3)
dezenas = sorted(sample(range(init, fim),qdezenas))
print(f'\033[0;31m{qdezenas} Dezenas Sorteadas ==> {dezenas}')
print(f'O Mês escolhido foi: {mesecolhido}' if loto == 6 else '-='*50)
print('-='*42 if loto == 6 else '')
