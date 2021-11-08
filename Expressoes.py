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
    def analisar(string):
        pilha = Pilha()

        for item in string:
            if item == '(':
                pilha.empilhar(item)
            elif item == ')':
                if pilha.topo() == '(':
                    pilha.desempilhar()
                else:
                    pilha.empilhar(')')

            elif item == '[':
                pilha.empilhar(item)
            elif item == ']':
                if pilha.topo() == '[':
                    pilha.desempilhar()
                else:
                    pilha.empilhar(']')

            elif item == '{':
                pilha.empilhar(item)
            elif item == '}':
                if pilha.topo() == '{':
                    pilha.desempilhar()
                else:
                    pilha.empilhar('}')

        if pilha.topo() != None:
            print("N")
        else:
            print("S")

for a in range(int(input())):  
    string = str(input())
    ParenthesisBalancer.analisar(string)