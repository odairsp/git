file = open("a2.txt", "a")

for x in range(1, 16):
    file.write("%i. frase: " % x + input("Digite a %i. frase:  " % x)+ "\n")
file.close()

file = open("a2.txt", "r")

for x in file:
    if int(x.split(". ")[0]) % 2 != 0:
        print(x, end="")

file.close()
