from biblioteca_grafo import Grafo

def resultado(grafo):
    for i in range(1, grafo.qtdVertices() + 1):
        print("%d: " % (i), end = " ")
        for j in range(1, grafo.qtdVertices() + 1):
            print(grafo.peso2(i, j), end = ' ')
        print()

    print("\ninf: Representa uma aresta de peso que não existe, ou seja, infinito")

def floydwarshall(grafo):
    for k in range (1, grafo.qtdVertices() + 1):
        for i in range (1, grafo.qtdVertices() + 1):
            for j in range (1, grafo.qtdVertices() + 1):
                grafo.pesos[(i,j)] = min(grafo.peso2(i,j), grafo.peso2(i,k) + grafo.peso2(k,j))

    return grafo

if __name__ == "__main__":
    grafo = Grafo("./fln_pequena.txt", True)
    resultado(floydwarshall(grafo))