'''
Conversão de Tempo
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado 
evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para
horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada
556

Exemplo de Saída
0:9:16
'''

segundos = int(input())

hora = segundos // 3600
segundos -= hora * 3600
minutos = segundos // 60
segundos -= minutos * 60

print("%i:%i:%i" % (hora, minutos, segundos))
