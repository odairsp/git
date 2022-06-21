'''
Sequencia IJ 3
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''

cont1 = 7
cont2 = 4
for i in range(1, 10):
    if i % 2 == 1:
        for j in range(cont1, cont2, -1):
            print("I=%i J=%i" % (i, j))
        cont1 += 2
        cont2 += 2

