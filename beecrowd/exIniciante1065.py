'''
Pares entre Cinco Números
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada	Exemplo de Saída
7                   3 valores pares
-5
6
-4
12
'''
pares = 0

for x in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
print("%i valores pares" % pares)
