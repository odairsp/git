'''
Sequencia IJ 4
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''
i = 0
j = 0
while i <= 2:
    i = round(i, 1)
    for j in range(1, 4):
        if i == 2.0 or i == 0 or i == 1.0:

            print("I=%i J=%i" % (i, j+i))
        else:
            print("I=%.1f J=%.1f" % (i, j+i))
    i += 0.2
    
