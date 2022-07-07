

s = "S"

try:
    print(int(s))
except ValueError as e:
    print(e.args[0])