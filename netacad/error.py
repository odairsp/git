class Pilha:
    def __init__(self):
        self.__lista = []


    def push(self, val):
        self.__lista.append(val)


    def pop(self):
        val  = self.__lista[-1]
        del self.__lista[-1]
        return val


class SubClassePilha(Pilha):
    def __init__(self):
        Pilha.__init__(self)
        self.__sum = 0


    def get_sum(self):
        return self.__sum


    def push(self, val):
        self.__sum += val
        Pilha.push(self, val)

    
    def pop(self):
        val = Pilha.pop(self)
        self.__sum -= val
        return val


novaPilha = SubClassePilha()

for i in range(5):
    novaPilha.push(i)
print(novaPilha.get_sum())

for i in range(5):
    
    print(novaPilha.pop())

