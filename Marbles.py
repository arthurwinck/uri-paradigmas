def encontrarMarble(query, lista_marbles, count):
    p = int(len(lista_marbles)/2)
    r = lista_marbles[p]

    if p == 0 and r != query:
        print(f"{query} not found")
        return

    if query == r:
        print(f"{query} found at {p+count+1}")
        return

    if query > r:
        encontrarMarble(query, lista_marbles[p:], p + count)

    else:
        encontrarMarble(query, lista_marbles[:p], count)


while True:
    num_marbles, num_queries = map(int, input().split())

    if num_marbles == 0 and num_queries == 0:
        break

    lista_marbles = []
    
    for a in range(num_marbles + num_queries):
        
        if a < num_marbles:
            lista_marbles.append(int(input()))

        if a == (num_marbles - 1):
            lista_marbles.sort()
        
        if a >= num_marbles:
            query = int(input())
            print(f"CASE# {a-num_marbles+1}:")
            encontrarMarble(query, lista_marbles, 0)