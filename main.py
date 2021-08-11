'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

v = int(input('Digite a quantidade de vertices: '))

def criar_matriz():
    for i in range(v):
        novaLinha = []
        for j in range(v):
            novaLinha.append(0)
        grafo.append(novaLinha)

def mostrar_matriz():
    for i in range(v):
        for j in range(v):
            print(grafo[i][j], end=" ")
        print("")

def adicionar_aresta(l, c):
    grafo[l-1][c-1] += 1
    grafo[c-1][l-1] += 1

grafo = []
criar_matriz()
mostrar_matriz()

x = input('Adicionar uma aresta? [s/n] ')
while x != 'n':
    l = int(input('Digite os vértices a ligar: '))
    c = int(input(''))
    adicionar_aresta(l, c)
    x = input('Adicionar uma aresta? [s/n] ')
mostrar_matriz()

grau = []
for i in range(v):
    grau.append(0)
for i in range(v):
    grau[i] = grau[i] + grafo[i][0]
    print('O grau do vértice', i+1, 'é', grau[i])

maximo = 0
for i in range(v):
    for j in range(v):
        if grafo[i][j] > maximo:
            maximo = grafo[i][j]
print('O grau maximo é: ', maximo)

minimo = maximo        
for i in range(v):
    for j in range(v):
        if (grafo[i][j] < minimo) and (grafo[i][j] != 0):
            minimo = grafo[i][j]
print('O grau mínimo é: ', minimo)

