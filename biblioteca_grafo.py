class Grafo:
    def __init__(self, file_name):
        self.file_name = file_name
        self.vertices = []
        self.arestas  = []
        self.pesos    = {}
        self.num_vertices = None
        self.num_arestas  = None
        self.read_data()

    def qtdVertices(self):
        return self.num_vertices

    def qtdArestas(self):
        return self.num_arestas

    def grau(self, v):
        grau = 0
        for aresta in self.arestas:
            if v in aresta:
                grau += 1
        return grau
    
    def rotulo(self, v):
        return self.vertices[v - 1]
    
    def vizinhos(self, v):
        vizinhos = []
        for aresta in self.arestas:
            if v in aresta:
                vetor_aux = aresta.copy()
                vetor_aux.remove(v)
                vizinhos.append(vetor_aux[0])
        return vizinhos
    
    def haHaresta(self, u, v):
        for aresta in self.arestas:
            if set([u, v]) == set(aresta):
                return True
        return False

    def peso(self, u, v):
        existe = False
        tupla = None
        for aresta in self.arestas:
            if set([u, v]) == set(aresta):
                existe = True
                tupla = tuple(aresta)
        if existe:
            return self.pesos[tupla]
        else:
            return float("inf")
    
    def read_data(self):
        with open(self.file_name) as f:
            conteudo_grafo = f.readlines()
        
        primeira_linha = conteudo_grafo[0].split()
        self.num_vertices = int(primeira_linha[1])
        
        for i in range(self.num_vertices):
            linha = conteudo_grafo[i + 1].split()
            self.vertices.append(linha[1])
        
        i += 3
        for j in range(i, len(conteudo_grafo)):
            linha = conteudo_grafo[j].split()
            aresta = [int(linha[0]), int(linha[1])]
            self.arestas.append(aresta)
            self.pesos[tuple(aresta)] = float(linha[2])
        self.num_arestas = len(self.arestas)
    

grafo1 = Grafo("dolphins.txt")
print(grafo1.peso(1,41))
