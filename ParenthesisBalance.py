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

class ParenthesisBalancer:
    def __init__(self, string):
        self.pilha = Pilha()
        self.string = string

        self.analisar()

    def analisar(self):
        for item in self.string:
            if item == '(':
                self.pilha.empilhar(item)
            elif item == ')':
                if self.pilha.topo() == '(':
                    self.pilha.desempilhar()
                else:
                    self.pilha.empilhar(')')

        if self.pilha.topo() != None:
            print("incorrect")
        else:
            print("correct")
        
while True:
    try:
        string = str(input())
        ParenthesisBalancer(string)
    except EOFError:
        break
