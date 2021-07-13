from biblioteca_grafo import Grafo

def resultado(grafo):
    print(grafo.pesos)
    print("\nRepresenta uma aresta de peso que não existe, ou seja, infinito")

def floydwarshall(grafo):
    for a in range (grafo.qtdVertices()):
        for b in range (grafo.qtdVertices()):
            for c in range (grafo.qtdVertices()):
                grafo.pesos[(b,c)] = min(grafo.peso(b,c), grafo.peso(b,a) + grafo.peso(a,c))
    return grafo

if __name__ == "__main__":
    grafo = Grafo("./fln_pequena.txt")
    resultado(floydwarshall(grafo))