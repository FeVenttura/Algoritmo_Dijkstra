from collections import defaultdict

class Grafo():
    def __init__(self):
        self.arestas = defaultdict(list)
        self.pesos = {}
    
    def adiciona_aresta(self, no_inicio, no_final, peso):
        self.arestas[no_inicio].append(no_final)
        self.arestas[no_final].append(no_inicio)
        self.pesos[(no_inicio, no_final)] = peso
        self.pesos[(no_final, no_inicio)] = peso


def Dijsktra(grafo, inicial, final):
    caminho_curto = {inicial: (None, 0)}
    no_atual = inicial
    visitado = set()
    
    while no_atual != final:
        visitado.add(no_atual)
        destinos = grafo.arestas[no_atual]
        peso_nodo_atual = caminho_curto[no_atual][1]

        for proximo_no in destinos:
            peso = grafo.pesos[(no_atual, proximo_no)] + peso_nodo_atual
            if proximo_no not in caminho_curto:
                caminho_curto[proximo_no] = (no_atual, peso)
            else:
                current_shortest_weight = caminho_curto[proximo_no][1]
                if current_shortest_weight > peso:
                    caminho_curto[proximo_no] = (no_atual, peso)
        
        proximos_destinos = {vertice: caminho_curto[vertice] for vertice in caminho_curto if vertice not in visitado}
        if not proximos_destinos:
            return "Rota impossível"
        no_atual = min(proximos_destinos, key=lambda k: proximos_destinos[k][1])
    
    caminho = []
    while no_atual is not None:
        caminho.append(no_atual)
        proximo_no = caminho_curto[no_atual][0]
        no_atual = proximo_no
        
    caminho = caminho[::-1]
    return caminho
 


grafo = Grafo()

arestas = [
    ('A', 'B', 7),
    ('A', 'C', 9),
    ('A', 'F', 14),
    ('B', 'C', 10),
    ('B', 'D', 15),
    ('C', 'D', 11),
    ('C', 'F', 2),
    ('D', 'E', 6),
    ('E', 'F', 9)
]

for aresta in arestas:
    grafo.adiciona_aresta(*aresta)

combinacoes = [
    ['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
    ['B', 'C'], ['B', 'D'], ['B', 'E'], ['B', 'F'],
    ['C', 'D'], ['C', 'E'], ['C', 'F'],
    ['D', 'E'], ['D', 'F'],
    ['E', 'F']
]

todos_caminhos = []

for i in range(len(combinacoes)):
    caminho = Dijsktra(grafo, combinacoes[i][0], combinacoes[i][1])
    todos_caminhos.append(caminho)
    print("Caminho de " + combinacoes[i][0] + " para " + combinacoes[i][1] + " : ")
    print(caminho)
