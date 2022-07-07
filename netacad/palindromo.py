palavra =  input("Digite a palavra ou texto: ")
palavra2 = palavra.split()
palavra3 = ""
for x in palavra2:
    palavra3 += x.upper()

palavra2 = palavra3[::-1]
if len(palavra2) < 1:
    print("Não é palindromo!")
    exit()

for x in range(len(palavra3)):
    print("["+palavra2[x]+"]")
    if palavra2[x] != palavra3[x] or len(palavra2) < 1:
        print("Não é palindromo!")
        exit()
print("É palindromo!")   