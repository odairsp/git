'''
Soma de Impares Consecutivos I
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos 
números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores 
ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada	Exemplo de Saída
6                   5
-5

15                  13
12

12                 0 
12


'''

a = int(input())
b = int(input())
c = [a,b]

c.sort()
soma = 0
for x in range(c[0]+1, c[1]):
    if x % 2 == 1 :
        soma += x

print(soma)




