# 1005
'''
a = float(input())
b = float(input())

media = ((a*3.5)+(b*7.5))/11.0

print("MEDIA = %.5f" % media)
'''

# 1007
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

DIFERENCA = (a * b - c * d)

print("DIFERENCA =", DIFERENCA)
'''
# 1008

'''Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. 
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, 
quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. 
No caso do salário, também deve haver um espaço em branco após o $.

Exemplos de Entrada	Exemplos de Saída
25
100
5.50

NUMBER = 25
SALARY = U$ 550.00'''


NUMBER = int(input())
HOURS = int(input())
VALOR_HORA = float(input())

SALARY = HOURS * VALOR_HORA

print("NUMBER =", NUMBER)
print("SALARY = U$ %.2f" % SALARY)
