from biblioteca_grafo import Grafo

inf = 99999

def Dijkstra(grafo,vertice_origem):
    if vertice_origem < 0 or vertice_origem >= grafo.qtdVertices():
        return "Impossivel"
    else:
        distancias = {vertice: inf for vertice in range(grafo.qtdVertices()+1)}
        caminhos = {vertice: None for vertice in range(grafo.qtdVertices()+1)}
        distancias[vertice_origem] = 0
        vertices = list(map(int,grafo.vertices.copy()))


        while (len(vertices)) != 0:
            menor_custo = min(vertices,key=lambda vertice: distancias[vertice])

            if distancias[menor_custo] == inf:
                break
            else:
                vizinhos = []
                for vert in grafo.vizinhos(menor_custo):
                    if vert in vertices:
                        vizinhos.append(vert)

                for vertice in vizinhos:
                    melhor_caminho = distancias[menor_custo] + grafo.peso(menor_custo,vertice)
                    if melhor_caminho < distancias[vertice]:
                        distancias[vertice] = melhor_caminho
                        caminhos[vertice] = menor_custo
                
                vertices.remove(menor_custo)
        
        for proximo, origem in caminhos.items():
            caminho = []
            if not proximo:
                continue  
            while origem != None:
                caminho.insert(0,origem)
                origem = caminhos[origem]
                
            caminho.append(proximo)
            caminho = [str(string) for string in caminho]

            print("%d: "%(proximo),end=" ")
            print(",".join(caminho),end="")
            print("; d=%.2f"%distancias[proximo])

grafo1 = Grafo("dolphins.txt")
Dijkstra(grafo1,1)
