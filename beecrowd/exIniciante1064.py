''' 
Positivos e Média
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram 
positivos. Na próxima linha, deve-se mostrar a média de todos os valores 
positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto 
flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima 
linha deve mostrar a média dos valores positivos digitados.

Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5                  7.4
6
-3.4
4.6
12
'''
positivos = []
for x in range(6):
    entrada = float(input())
    if entrada > 0:
        positivos.append(entrada)

print("%i valores positivos" % len(positivos))
print("%.1f" % (sum(positivos) / len(positivos)))
