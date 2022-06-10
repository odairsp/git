'''
Notas e Moedas
Por Neilor Tonin URI  Brasil

Timelimit: 1
Leia um valor de ponto flutuante com duas casas decimais. 
Este valor representa um valor monetário. A seguir calcule o menor 
número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100 50 20 10 5 2. As moedas possíveis 
são de 1 0.50 0.25 0.10 0.05 e 0.01. A seguir mostre a relação de 
notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante 
N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o 
valor inicial conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	
576.73

Exemplo de Saída
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
'''

d = float(input())

c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
m1 = 0
m50 = 0
m25 = 0
m10 = 0
m05 = 0
m01 = 0

while(d > 0):
    d = round(d, 2)
    if (d >= 100):
        c100 += 1
        d -= 100
    elif(d >= 50):
        c50 += 1
        d -= 50.0
    elif(d >= 20):
        c20 += 1
        d -= 20
    elif(d >= 10):
        c10 += 1
        d -= 10
    elif(d >= 5):
        c5 += 1
        d -= 5
    elif(d >= 2):
        c2 += 1
        d -= 2
    elif(d >= 1):
        m1 += 1
        d -= 1.0
    elif(d >= 0.50):
        m50 += 1
        d -= 0.50
    elif(d >= 0.25):
        m25 += 1
        d -= 0.25
    elif(d >= 0.10):
        m10 += 1
        d -= 0.10
    elif(d >= 0.05):
        m05 += 1
        d -= 0.05
    elif(d >= 0.01):
        m01 += 1
        d -= 0.01
    else:
        d = -1
print("NOTAS:")
print("%i nota(s) de R$ 100.00" % c100)
print("%i nota(s) de R$ 50.00" % c50)
print("%i nota(s) de R$ 20.00" % c20)
print("%i nota(s) de R$ 10.00" % c10)
print("%i nota(s) de R$ 5.00" % c5)
print("%i nota(s) de R$ 2.00" % c2)


print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % m1)
print("%i moeda(s) de R$ 0.50" % m50)
print("%i moeda(s) de R$ 0.25" % m25)
print("%i moeda(s) de R$ 0.10" % m10)
print("%i moeda(s) de R$ 0.05" % m05)
print("%i moeda(s) de R$ 0.01" % m01)
