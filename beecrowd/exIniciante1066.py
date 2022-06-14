'''
Pares, Ímpares, Positivos e Negativos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram 
positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, 
não esquecendo o final de linha após cada uma.

Exemplo de Entrada	Exemplo de Saída
-5                  3 valor(es) par(es)
0                   2 valor(es) impar(es)
-3                  1 valor(es) positivo(s)
-4                  3 valor(es) negativo(s)
12                  
'''

pares = 0
impares = 0
positivos = 0
negativos = 0

for x in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print("%i valor(es) par(es)" % pares)
print("%i valor(es) impar(es)" % impares)
print("%i valor(es) positivo(s)" % positivos)
print("%i valor(es) negativo(s)" % negativos)
