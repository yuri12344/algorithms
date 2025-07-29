"""
Min/Max Heap Implementation

Heaps binários para priority queues e algoritmos
Implementado com arrays para eficiência O(log n)
"""


class MinHeap:
    """
    Min Heap - menor elemento no topo
    
    Usa array interno para representar árvore binária completa
    
    Métodos FAANG:
    - Insert O(log n)
    - Extract min O(log n)
    - Heapify O(n)
    - Top k elements
    """
    
    def __init__(self):
        """
        Inicializa heap vazio
        
        TODO:
        - self.heap = []
        - self.size = 0
        """
        pass
    
    def parent(self, index):
        """
        Índice do pai
        
        Args:
            index: Índice do filho
        
        Returns:
            int: Índice do pai ou None se raiz
        
        TODO: Implementar fórmula (i-1)//2
        """
        pass
    
    def left_child(self, index):
        """
        Índice do filho esquerdo
        
        Args:
            index: Índice do pai
        
        Returns:
            int: Índice do filho ou None se não existe
        
        TODO: Implementar fórmula 2*i + 1
        """
        pass
    
    def right_child(self, index):
        """
        Índice do filho direito
        
        Args:
            index: Índice do pai
        
        Returns:
            int: Índice do filho ou None se não existe
        
        TODO: Implementar fórmula 2*i + 2
        """
        pass
    
    def insert(self, value):
        """
        Insere valor no heap
        
        Args:
            value: Valor a inserir
        
        TODO:
        - Adicionar no final
        - Heapify up
        - Atualizar size
        
        Time: O(log n)
        """
        pass
    
    def extract_min(self):
        """
        Remove e retorna o menor elemento
        
        Returns:
            int: Menor elemento ou None se vazio
        
        TODO:
        - Trocar com último elemento
        - Remover último
        - Heapify down
        - Atualizar size
        
        Time: O(log n)
        """
        pass
    
    def peek(self):
        """
        Olha o menor elemento sem remover
        
        Returns:
            int: Menor elemento ou None se vazio
        
        TODO: Retornar heap[0] ou None
        """
        pass
    
    def heapify_up(self, index):
        """
        Restaura propriedade heap subindo
        
        Args:
            index: Índice para começar
        
        TODO:
        - Comparar com pai
        - Trocar se menor
        - Continuar até raiz
        """
        pass
    
    def heapify_down(self, index):
        """
        Restaura propriedade heap descendo
        
        Args:
            index: Índice para começar
        
        TODO:
        - Encontrar menor filho
        - Trocar se maior que filho
        - Continuar até folha
        """
        pass
    
    def build_heap(self, values):
        """
        Constrói heap a partir de array O(n)
        
        Args:
            values: Lista de valores
        
        TODO:
        - Copiar valores
        - Heapify down do meio para trás
        
        Time: O(n)
        """
        pass
    
    def is_empty(self):
        """
        Verifica se heap está vazio
        
        Returns:
            bool: True se vazio
        
        TODO: Verificar size
        """
        pass
    
    def size(self):
        """
        Tamanho do heap
        
        Returns:
            int: Número de elementos
        
        TODO: Retornar size
        """
        pass
    
    def __len__(self):
        """
        Tamanho do heap (mágico Python)
        
        Returns:
            int: Número de elementos
        """
        pass
    
    def __str__(self):
        """
        Representação em nível
        
        Returns:
            str: Heap formatado por nível
        """
        pass


class MaxHeap(MinHeap):
    """
    Max Heap - maior elemento no topo
    
    TODO: Estender MinHeap trocando comparações
    """
    
    def extract_max(self):
        """
        Remove e retorna o maior elemento
        
        Returns:
            int: Maior elemento ou None se vazio
        
        TODO: Chamar extract_min mas inverter comparações
        """
        pass
    
    def peek(self):
        """
        Olha o maior elemento sem remover
        
        Returns:
            int: Maior elemento ou None se vazio
        """
        pass
    
    def heapify_up(self, index):
        """
        Restaura propriedade max heap subindo
        
        Args:
            index: Índice para começar
        
        TODO: Inverter comparações (maior que pai)
        """
        pass
    
    def heapify_down(self, index):
        """
        Restaura propriedade max heap descendo
        
        Args:
            index: Índice para começar
        
        TODO: Inverter comparações (menor que filho)
        """
        pass