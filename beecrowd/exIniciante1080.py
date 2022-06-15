'''
Maior e Posição
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 100 valores inteiros. Apresente então o maior valor lido e a 
posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e 
distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme 
exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
2
113
45
34565
6
...
8
 

34565
4
'''
numeros = []
for x in range(100):
    numeros.append(int(input()))

maior = max(numeros)
posicao = numeros.index(maior)

print(maior)
print(posicao+1)
