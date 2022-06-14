''' 
Números Positivos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5
6
-3.4
4.6
12


'''
pos = 0

for x in range(6):
    valor = float(input())
    if valor > 0:
        pos += 1
print("%i valores positivos" % pos)
