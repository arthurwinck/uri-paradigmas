class Pilha:
    def __init__(self):
        self.lista = []

    def empilhar(self, item):
        self.lista.append(item)

    def desempilhar(self):
        return self.lista.pop()

    def topo(self):
        if len(self.lista) == 0:
            return None
        
        return self.lista[-1]

class Minerador:
    def __init__(self, string):
        self.pilha = Pilha()
        self.string = string
        self.diamantes = 0

        self.minerar()

    def minerar(self):
        for item in self.string:
            if item == '<':
                self.pilha.empilhar(item)
            elif item == '>':
                if self.pilha.topo() == '<':
                    self.pilha.desempilhar()
                    self.diamantes += 1

        print(self.diamantes)

num = int(input())
for i in range(num):
    minerador = Minerador(str(input()))
