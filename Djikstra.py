import math


class HeapMin:

    def __init__(self):
        self.node = 0
        self.heap = []

    def add_node(self, u, indice):
        self.heap.append([u, indice])
        self.node += 1
        f = self.node
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def show_heap(self):
        nivel = int(math.log(self.node, 2))
        x = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                x += 1
            print('')
        for i in range(self.node-x):
            print(f'{self.heap[a]}', end='  ')
            x += 1
        print('')

    def remove_node(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.node - 1]
        self.heap.pop()
        self.node -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.node:
                break
            if f + 1 <= self.node:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.node

    def menor_elemento(self):
        if self.node != 0:
            return self.heap[0]
        return 'Arvore vazia'

    def filho_esquerda(self, u):
        if self.node >= 2*u:
            return self.heap[2*u-1]
        return 'Esse nó não tem filho'

    def filho_direita(self, u):
        if self.node >= 2*u+1:
            return self.heap[2*u]
        return 'Esse nó não tem filho da direita'

    def pai(self, u):
        return self.heap[u // 2]


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('Matriz de adjacências: ')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.add_node(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_node()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.add_node(dist + self.grafo[v-1][i], i+1)
        return custo_vem




print ("=-==-==-==-==MENU==-==-==-==-=")
opt = str(input('Gerar grafo? s/n '))
if opt == 's':
    vertices = int(input('Digite o numero de vertices: '))
    g = Grafo(vertices)
else:
    exit(0)
op = 's'
while op != 'n':
    op = str(input('Deseja adicionar uma aresta? s/n '))
    if op == 's':
        x = int(input('Digite os vertices a ligar: '))
        y = int(input())
        z = int(input('Digite o peso da aresta: '))
        g.adiciona_aresta(x, y, z)
    else:
        break

#g = Grafo(6)
#g.adiciona_aresta(1, 2, 4)
#g.adiciona_aresta(1, 3, 4)
#g.adiciona_aresta(2, 3, 2)
#g.adiciona_aresta(3, 4, 3)
#g.adiciona_aresta(3, 5, 6)
#g.adiciona_aresta(3, 6, 1)
#g.adiciona_aresta(4, 5, 2)
#g.adiciona_aresta(5, 6, 3)


g.mostra_matriz()

resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)
