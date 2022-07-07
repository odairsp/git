palavra1 = sorted(list(input("Digite a palavra 1: ").upper()))
palavra2 = sorted(list(input("Digite a palavra 2: ").upper()))


for x in range(len(palavra1)):
    if palavra1[x] != palavra2[x]:
        print("Não")
        exit()
print("é")