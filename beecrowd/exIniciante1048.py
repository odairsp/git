'''
Aumento de Salário
Por Neilor Tonin, URI  Brasil

Timelimit: 1
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	                Percentual de Reajuste
0 - 400.00              15%
400.01 - 800.00         12%
800.01 - 1200.00        10%
1200.01 - 2000.00       7%
Acima de 2000.00        4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem 
como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas 
decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	        Exemplo de Saída
400.00                      Novo salario: 460.00
                            Reajuste ganho: 60.00
                            Em percentual: 15 %

800.01                      Novo salario: 880.01
                            Reajuste ganho: 80.00
                            Em percentual: 10 %

2000.00                     Novo salario: 2140.00
                            Reajuste ganho: 140.00
                            Em percentual: 7 %

'''
salario = float(input())

if (salario >= 0.0) and (salario <= 400.00):
    print("Novo salario: %.2f" % (salario*1.15))
    print("Reajuste ganho: %.2f" % (salario*0.15))
    print(f"Em percentual: {15} %")
elif (salario > 400.0) and (salario <= 800.00):
    print("Novo salario: %.2f" % (salario*1.12))
    print("Reajuste ganho: %.2f" % (salario*0.12))
    print(f"Em percentual: {12} %")
elif (salario > 800.0) and (salario <= 1200.00):
    print("Novo salario: %.2f" % (salario*1.10))
    print("Reajuste ganho: %.2f" % (salario*0.10))
    print(f"Em percentual: {10} %")
elif (salario > 1200.0) and (salario <= 2000.00):
    print("Novo salario: %.2f" % (salario*1.07))
    print("Reajuste ganho: %.2f" % (salario*0.07))
    print(f"Em percentual: {7} %")
elif salario > 2000.0:
    print("Novo salario: %.2f" % (salario*1.04))
    print("Reajuste ganho: %.2f" % (salario*0.04))
    print(f"Em percentual: {4} %")
