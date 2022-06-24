file1 = open("a1.txt", "a")
file2 = open("a2.txt", "r")

for x in file2:
    y = x.split(". ")
    if int(y[0]) % 2 == 0:
        file1.write(x)

file1.close()
file2.close()
