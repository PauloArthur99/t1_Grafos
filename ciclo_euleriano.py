from os import truncate
from biblioteca_grafo import Grafo


def buscarSubCicloEuleriano(grafo, v, arestas_visitadas):
    ciclo = [v]
    target = v

    while True:
        vizinhos = grafo.vizinhos(v)
        aresta_livre = False
        for u in vizinhos:
            aresta = [v, u]
            aresta = tuple(set(aresta))
            if not(arestas_visitadas[aresta]):
                aresta_livre = True
                vertice_destino = u
                prox_aresta = aresta

        if not(aresta_livre):
            return (False, ciclo)
        else:
            arestas_visitadas[prox_aresta] = True
            v = vertice_destino
            ciclo.append(v)

        if v == target:
            break
    
    for i in range(len(ciclo)):
        u = ciclo[i]
        vizinhos = grafo.vizinhos(u)
        for vertice in vizinhos:
            aresta = [u, vertice]
            aresta = tuple(set(aresta))
            aresta_livre = False
            if not(arestas_visitadas[aresta]):
                aresta_livre = True
                break
        if aresta_livre:
            r, ciclo_linha = buscarSubCicloEuleriano(grafo, u, arestas_visitadas)
            if not(r):
                return(False, ciclo)
            ciclo.pop(i)
            for elem in ciclo_linha:
                ciclo.insert(i, elem)
                i += 1
    return(True, ciclo)


def ciclo_euleriano(grafo):
    arestas_visitadas = {}

    for i in range(1, grafo.qtdVertices() + 1):
        vizinhos = grafo.vizinhos(i)
        for v in vizinhos:
            aresta = [i, v]
            aresta = tuple(set(aresta))
            arestas_visitadas[aresta] = False
            vert_arbit = i
    
    r, ciclo = buscarSubCicloEuleriano(grafo, vert_arbit, arestas_visitadas)
    
    if not(r):
        print(0)
        for i in range(len(ciclo) - 1):
            print(ciclo[i],", ", sep='', end='')
        print(ciclo[-1])
        return
    else:
        for i in range(1, grafo.qtdVertices() + 1):
            vizinhos = grafo.vizinhos(i)
            for v in vizinhos:
                aresta = [i, v]
                aresta = tuple(set(aresta))
                if not(arestas_visitadas[aresta]):
                    print(0)
                    for i in range(len(ciclo) - 1):
                        print(ciclo[i],", ", sep='', end='')
                    print(ciclo[-1])
                    return
        print(1)
        for i in range(len(ciclo) - 1):
            print(ciclo[i],", ", sep='', end='')
        print(ciclo[-1])
        return 


grafo1 = Grafo("teste_euleriano.txt")
ciclo_euleriano(grafo1)

