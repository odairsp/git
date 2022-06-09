''' 
Idade em Dias
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia um valor inteiro correspondente à idade de uma pessoa em dias e 
informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e 
todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que 
permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático 
simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada	
400
Exemplo de Saída
1 ano(s)
1 mes(es)
5 dia(s)
'''

dias = int(input())

ano = dias // 365
dias -= ano * 365
mes = dias // 30
dias -= mes * 30

print("%i ano(s)\n%i mes(es)\n%i dia(s)" % (ano, mes, dias))
