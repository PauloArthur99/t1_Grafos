from biblioteca_grafo import Grafo

def resultado(grafo):
    #for i in range(grafo.qtdVertices()):
        #print("%d: " % (i + 1)) + ",".join(map(str, grafo.pesos[(i,i)])))
    #print(grafo.pesos[(1,2)])
    for i in range(grafo.qtdVertices()):
        print("Peso: %.1f" % grafo.peso(1,i+1))
        print("Pesos: %.1f" % grafo.pesos[(1,i+1)])
        print("\n")

    print("\nRepresenta uma aresta de peso que não existe, ou seja, infinito")

def floydwarshall(grafo):
    for k in range (grafo.qtdVertices()):
        for i in range (grafo.qtdVertices()):
            for j in range (grafo.qtdVertices()):
                grafo.pesos[(i,j)] = min(grafo.peso(i,j), grafo.peso(i,k) + grafo.peso(k,j))
    return grafo

if __name__ == "__main__":
    grafo = Grafo("./fln_pequena.txt")
    resultado(floydwarshall(grafo))