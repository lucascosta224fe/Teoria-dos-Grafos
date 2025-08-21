from Grafo import Grafo

class GrafoDenso(ABC):

    def __init__(self, vertices):
        self.vertices_list = vertices
        self.num_de_vertices = len(self.vertices_list)
        self.grafodenso = [[0] * self.num_de_vertices for i in range(self.num_de_vertices)]
        self.num_aresta = 0

    def numero_de_vertices(self):
        print(f'Número de vértices: {self.num_de_vertices}')

    def numero_de_arestas(self):
        print(f'Número de arestas: {self.num_aresta}')

    def sequencia_de_graus(self):
        graus = {}
        for i in range(self.num_de_vertices):
            grau = 0
            for j in range(self.num_de_vertices):
                if self.grafodenso[i][j] == 1:
                    grau += 1
            graus[i] = grau
        
        print(f'Sequência de graus: {sorted(graus.values())}')
        # return graus.values()
        

    def adicionar_aresta(self, u, v):
        u_idx = self.vertices_list.index(u)
        v_idx = self.vertices_list.index(v)
        
        self.grafodenso[u_idx][v_idx] = 1
        self.grafodenso[v_idx][u_idx] = 1
        print(f'Aresta adicionada entre {u} e {v}')

        self.num_aresta += 1
        

    def remover_aresta(self, u, v):
        u_idx = self.vertices_list.index(u)
        v_idx = self.vertices_list.index(v)

        self.grafodenso[u_idx][v_idx] = 0
        self.grafodenso[u_idx][v_idx] = 0
        print(f'Aresta removida entre {u} e {v}')

        self.num_aresta -= 1

    def  imprimir(self):
        print('Matriz de Adjacência: \n')
        for i in range(self.num_de_vertices):
            print(*self.grafodenso[i])
        print('\n')

V = ['A','B','C','D','E']
g = GrafoDenso(V)

# print(V)

g.adicionar_aresta('A','B')
g.adicionar_aresta('A','C')
g.adicionar_aresta('C','D')
g.adicionar_aresta('C','E')
g.adicionar_aresta('B','D')

g.imprimir()

g.numero_de_vertices()

g.numero_de_arestas()

g.sequencia_de_graus()

g.remover_aresta('A','C')

g.imprimir()
