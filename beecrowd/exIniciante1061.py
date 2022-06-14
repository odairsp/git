''' 
Tempo de um Evento
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. 
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta 
linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23        3 dia(s)
                    22 hora(s)
                    1 minuto(s)
                    0 segundo(s)
'''

diaI = input().split()
diaI = int(diaI[1])
horaI, minI, segI = [int(x) for x in input().split(" : ")]
diaF = input().split()
diaF = int(diaF[1])
horaF, minF, segF = [int(x) for x in input().split(" : ")]

if diaF == diaI:
    dia = 0
    hora = horaF - horaI
    min = minF - minI
    seg = segF - segI
elif diaF > diaI:
    dia = diaF - diaI - 1
    hora = horaF - horaI
    min = minF - minI
    seg = segF - segI
else:
    dia = 30 - diaI + diaF
    hora = 24 - horaI + horaF
    min = 60 - minI + minF
    seg = 60 - segI + segF

print("%i dia(s)" % dia)
print("%i hora(s)" % hora)
print("%i minuto(s)" % min)
print("%i segundo(s)" % seg)
