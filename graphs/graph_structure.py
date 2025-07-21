"""
Estruturas de Grafos com Listas de Adjacência

Implementações completas de grafos usando suas próprias estruturas:
- LinkedList para adjacency lists
- HashTable para mapeamento de vértices
- Queue/Stack para algoritmos

FAANG Graph Types:
- Undirected Graph
- Directed Graph  
- Weighted Graph
- Directed Acyclic Graph (DAG)
"""

from data_structures.lists import LinkedList, DoublyLinkedList
from data_structures.stacks import Stack
from data_structures.queues import Queue
from data_structures.hashing import HashTable

class GraphNode:
    """
    Nó de grafo com informações adicionais
    
    TODO: Implemente nó para uso em algoritmos de grafos
    Inclua: distance, parent, color, discovery_time, finish_time
    """
    
    def __init__(self, data):
        """
        TODO: Inicialize nó com dados e propriedades de algoritmos
        
        Propriedades essenciais:
        - data: valor do nó
        - distance: para BFS/Dijkstra
        - parent: para reconstruir caminhos
        - color: para DFS (white, gray, black)
        - discovery_time: tempo de descoberta DFS
        - finish_time: tempo de finalização DFS
        """
        pass
    
    def __str__(self):
        """TODO: String representation"""
        pass

class Edge:
    """
    Representação de aresta em grafo
    
    TODO: Implemente aresta com peso e direção
    """
    
    def __init__(self, source, destination, weight=1):
        """
        TODO: Inicialize aresta
        
        Propriedades:
        - source: vértice origem
        - destination: vértice destino
        - weight: peso da aresta (default=1)
        """
        pass
    
    def __str__(self):
        """TODO: String representation"""
        pass

class Graph:
    """
    Grafo não-direcionado com lista de adjacência
    
    TODO: Implemente grafo completo usando suas estruturas
    Use LinkedList para adjacency lists!
    """
    
    def __init__(self):
        """
        TODO: Inicialize grafo vazio
        
        Estrutura:
        - adjacency_list: HashTable de LinkedLists
        - vertices: HashTable de GraphNodes
        - edge_count: número de arestas
        """
        pass
    
    def add_vertex(self, vertex_id, data=None):
        """
        TODO: Adicione vértice ao grafo
        
        Complexidade: O(1)
        """
        pass
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """
        TODO: Adicione aresta não-direcionada
        
        Complexidade: O(1)
        
        Adiciona aresta em ambas as direções
        """
        pass
    
    def remove_edge(self, vertex1, vertex2):
        """
        TODO: Remova aresta do grafo
        
        Complexidade: O(degree)
        """
        pass
    
    def remove_vertex(self, vertex):
        """
        TODO: Remova vértice e todas suas arestas
        
        Complexidade: O(V + E)
        """
        pass
    
    def get_vertices(self):
        """
        TODO: Retorne todos os vértices
        
        Complexidade: O(V)
        """
        pass
    
    def get_edges(self):
        """
        TODO: Retorne todas as arestas
        
        Complexidade: O(V + E)
        """
        pass
    
    def get_neighbors(self, vertex):
        """
        TODO: Retorne vizinhos do vértice
        
        Complexidade: O(degree)
        """
        pass
    
    def has_edge(self, vertex1, vertex2):
        """
        TODO: Verifique se aresta existe
        
        Complexidade: O(degree)
        """
        pass
    
    def get_vertex_count(self):
        """
        TODO: Retorne número de vértices
        """
        pass
    
    def get_edge_count(self):
        """
        TODO: Retorne número de arestas
        """
        pass
    
    def __str__(self):
        """
        TODO: String representation do grafo
        """
        pass

class DirectedGraph(Graph):
    """
    Grafo direcionado
    
    TODO: Implemente grafo direcionado
    Herda de Graph mas arestas têm direção
    """
    
    def add_edge(self, source, destination, weight=1):
        """
        TODO: Adicione aresta direcionada
        
        Complexidade: O(1)
        
        Adiciona apenas de source para destination
        """
        pass
    
    def get_in_degree(self, vertex):
        """
        TODO: Retorne grau de entrada
        
        Complexidade: O(V + E)
        """
        pass
    
    def get_out_degree(self, vertex):
        """
        TODO: Retorne grau de saída
        
        Complexidade: O(1)
        """
        pass
    
    def reverse_graph(self):
        """
        TODO: Retorne grafo reverso (todas arestas invertidas)
        
        Complexidade: O(V + E)
        
        Usado em algoritmos como Kosaraju
        """
        pass

class WeightedGraph(Graph):
    """
    Grafo com pesos nas arestas
    
    TODO: Implemente grafo ponderado
    Extende Graph para incluir pesos
    """
    
    def add_edge(self, vertex1, vertex2, weight):
        """
        TODO: Adicione aresta com peso
        
        Complexidade: O(1)
        """
        pass
    
    def get_edge_weight(self, vertex1, vertex2):
        """
        TODO: Retorne peso da aresta
        
        Complexidade: O(degree)
        """
        pass
    
    def update_edge_weight(self, vertex1, vertex2, new_weight):
        """
        TODO: Atualize peso da aresta
        
        Complexidade: O(degree)
        """
        pass

class GraphUtils:
    """
    Utilitários para grafos
    
    TODO: Implemente métodos auxiliares
    """
    
    @staticmethod
    def create_random_graph(num_vertices, num_edges, directed=False, weighted=False):
        """
        TODO: Crie grafo aleatório para testes
        
        Complexidade: O(V + E)
        """
        pass
    
    @staticmethod
    def graph_to_adjacency_matrix(graph):
        """
        TODO: Converta para matriz de adjacência
        
        Complexidade: O(V²)
        """
        pass
    
    @staticmethod
    def adjacency_matrix_to_graph(matrix, directed=False, weighted=False):
        """
        TODO: Converta matriz para grafo
        
        Complexidade: O(V²)
        """
        pass
    
    @staticmethod
    def is_connected(graph):
        """
        TODO: Verifique se grafo é conectado
        
        Complexidade: O(V + E)
        """
        pass
    
    @staticmethod
    def count_connected_components(graph):
        """
        TODO: Conte número de componentes conectados
        
        Complexidade: O(V + E)
        """
        pass

class GraphExamples:
    """
    Exemplos de grafos para testes
    
    TODO: Crie grafos de exemplo
    """
    
    @staticmethod
    def create_sample_undirected_graph():
        """TODO: Grafo simples não-direcionado"""
        pass
    
    @staticmethod
    def create_sample_directed_graph():
        """TODO: Grafo simples direcionado"""
        pass
    
    @staticmethod
    def create_sample_weighted_graph():
        """TODO: Grafo simples ponderado"""
        pass
    
    @staticmethod
    def create_dag_example():
        """TODO: DAG para topological sort"""
        pass