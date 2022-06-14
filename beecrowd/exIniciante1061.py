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

datetime(1987, 12, 30, 17, 50, 14) #yr, mo, day, hr, min, sec

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
from datetime import date, datetime


diaI = input().split()
diaI = int(diaI[1])
horaI, minI, segI = [int(x) for x in input().split(" : ")]
diaF = input().split()
diaF = int(diaF[1])
horaF, minF, segF = [int(x) for x in input().split(" : ")]

inicial = datetime(2022, 1, diaI, horaI, minI, segI)
final = datetime(2022, 1, diaF, horaF, minF, segF)

total = final - inicial
segundos = total.seconds

horas = segundos // 3600
segundos -= horas * 3600
minutos = segundos // 60
segundos -= minutos * 60


print("%i dia(s)" % total.days)
print("%i hora(s)" % horas)
print("%i minuto(s)" % minutos)
print("%i segundo(s)" % segundos)
