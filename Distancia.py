lista = []
for a in range(2):
    a1,b1 = input().split()
    lista.append(float(a1))
    lista.append(float(b1))

distancia = ((lista[2]-lista[0])**2 + (lista[3]-lista[1])**2)**(1/2)
print(f"{round(distancia,4)}")