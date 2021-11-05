# Criação da classe do nó
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Classe para realizar operações da árvore
class Handler:

    def start(amount, num_list, num):
        originalHead = Node(num_list[0])

        for i in range(amount - 1):
            node = Node(num_list[i+1])
            head = originalHead
            
            Handler.insert(head, node)

        Handler.traverse(originalHead, num)

    def insert(head, node):
        if node.value > head.value:
            if head.right != None:
                Handler.insert(head.right, node)
            else:
                head.right = node
                return

        elif node.value < head.value:
            if head.left != None:
                Handler.insert(head.left, node)
            else:
                head.left = node
                return
        else:
            return

    def preorder(head, lista):
        
        if head:
            lista.append(head)
            Handler.preorder(head.left, lista)
            Handler.preorder(head.right, lista)

    def inorder(head, lista):
        
        if head:
            Handler.inorder(head.left, lista)
            lista.append(head)
            Handler.inorder(head.right, lista)

    def postorder(head, lista):
        
        if head:
            Handler.postorder(head.left, lista)
            Handler.postorder(head.right, lista)
            lista.append(head)

    def traverse(head, num):
        print(f'Case {num}:')

        lista_preorder = []
        Handler.preorder(head, lista_preorder)
        
        print('Pre.:', end = ' ')
        for no in lista_preorder:
            print(no.value, end=' ')

        lista_inorder = []
        Handler.inorder(head, lista_inorder)
        
        print('\nIn..:', end = ' ')
        for no in lista_inorder:
            print(no.value, end=' ')

        lista_postorder = []
        Handler.postorder(head, lista_postorder)
        
        print('\nPost:', end = ' ')
        for no in lista_postorder:
            print(no.value, end=' ')

        print("\n")


n_casos = int(input())
lista_lista_nos = []
lista_num_nos = []

for i in range(n_casos):
    num_nos = int(input())
    lista_num_nos.append(num_nos)
    lista_nos = list(map(int, input().split()))
    lista_lista_nos.append(lista_nos)
    
for i in range(n_casos):
    Handler.start(lista_num_nos[i], lista_lista_nos[i], i+1)