class Baralho:
    def __init__(self, quant):
        self.cartas = []
        self.cartas_descartadas = []
        self.iniciarProcedimento(int(quant))
        
    def pop(self):
        return self.cartas.pop()
        
    #Push diferente de uma pilha normal, já que a carta vai para o começo do baralho (mais embaixo)
    def push(self, carta):
        self.cartas.insert(0, carta)

    def povoarBaralho(self, quant):
        for i in range(quant):
            self.cartas.append(abs(i-quant))
        
    def iniciarProcedimento(self, quant):
        self.povoarBaralho(quant)

        while len(self.cartas) > 1:
            carta_descartada = self.pop()
            self.cartas_descartadas.append(carta_descartada)
            carta_base = self.pop()
            self.push(carta_base)

        print(f"Discarded cards: {', '.join(map(str,self.cartas_descartadas))}")
        print(f"Remaining card: {self.cartas[0]}")

while True:
    quantidade = input()
    if quantidade == '0':
        break
    baralho = Baralho(quantidade)