# abre em modo leitura
file2 = open("a2.txt", "r")

# copias as linhas para uma lista
filetemp = file2.readlines()

# fecha o arquivo
file2.close()

# abre em modo de escrita
file2 = open("a2.txt", "w")

# limpo o arquivo
file2.write("")
file2.close()

# abre em modo de acressimo de conteudo
file2 = open("a2.txt", "a")

# copia a lista filtrando, para o arquivo limpo
for linha in filetemp:
    y = linha.split(". ")
    if int(y[0]) % 2 != 0:
        file2.write(linha)
file2.close()

# copia o conteudo dos arquivos para listas
file1 = open("a1.txt", "r")
file2 = open("a2.txt", "r")
filetemp = file1.readlines()
filetemp += file2.readlines()
file1.close()
file2.close()
print(filetemp)
# transformo em dicionario
dicionario = {}
for linha in filetemp:
    dicionario[int(linha.split(". ")[0])] = linha

# pego a ordenação das chaves e imprimo os itens em ordem crescente
for x in sorted(dicionario):
    print(dicionario[x], end="")

print(dicionario.items())
