from biblioteca_grafo import Grafo

def busca_largura(grafo, vertice):
    if vertice < 0 or vertice >= grafo.qtdVertices():
        print("Impossivel")
        return 0
    
    else:
        visitados = [False] * (grafo.qtdVertices()+1)
        fila = []
        fila.append(vertice)
        distancia = 0
        
        while len(fila) != 0:
                nivel_atual = fila.copy()
                fila = []
                for vert in nivel_atual:
                    v = vert
                    visitados[v] = True
                    vizinhos_false = []
                    
                    for i in grafo.vizinhos(v):
                        if visitados[i] == False:
                            vizinhos_false.append(i)


                    for i in range(len(vizinhos_false)): 
                        visitados[vizinhos_false[i]] = True
                    fila.extend(vizinhos_false)
                
                nivel_atual = [str(string) for string in nivel_atual]
                print("%d:" % (distancia), end = ' ')
                print(",".join(nivel_atual))
                
                distancia += 1

grafo1 = Grafo("dolphins.txt")
busca_largura(grafo1,1)
