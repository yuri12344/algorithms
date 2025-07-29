"""
Segment Tree Implementation

Estrutura para queries de range (sum, min, max) com updates
O(log n) para ambos query e update
"""


class SegmentTree:
    """
    Segment Tree para queries de range
    
    Métodos FAANG:
    - Range sum/min/max query O(log n)
    - Point update O(log n)
    - Range update (lazy propagation)
    """
    
    def __init__(self, arr):
        """
        Inicializa segment tree com array
        
        Args:
            arr: Array de entrada
        
        TODO:
        - self.n = len(arr)
        - self.tree = [0] * (4 * self.n)
        - self.arr = arr
        - self.build(0, 0, self.n - 1)
        """
        pass
    
    def build(self, node, start, end):
        """
        Constrói segment tree recursivamente
        
        Args:
            node: Índice do nó atual
            start: Início do intervalo
            end: Fim do intervalo
        
        TODO:
        - Caso base: start == end
        - Recursivo: dividir ao meio
        - Combinar resultados
        
        Time: O(n)
        """
        pass
    
    def query_sum(self, left, right):
        """
        Soma do subarray [left, right]
        
        Args:
            left: Índice inicial
            right: Índice final
        
        Returns:
            int: Soma do intervalo
        
        TODO: Implementar query recursiva
        """
        pass
    
    def query_min(self, left, right):
        """
        Mínimo do subarray [left, right]
        
        Args:
            left: Índice inicial
            right: Índice final
        
        Returns:
            int: Mínimo do intervalo
        
        TODO: Implementar query recursiva
        """
        pass
    
    def query_max(self, left, right):
        """
        Máximo do subarray [left, right]
        
        Args:
            left: Índice inicial
            right: Índice final
        
        Returns:
            int: Máximo do intervalo
        
        TODO: Implementar query recursiva
        """
        pass
    
    def update_point(self, index, value):
        """
        Atualiza valor em índice específico
        
        Args:
            index: Índice a atualizar
            value: Novo valor
        
        TODO:
        - Atualizar folha
        - Propagar mudança para cima
        
        Time: O(log n)
        """
        pass
    
    def _query_range(self, node, start, end, left, right, operation):
        """
        Query genérica para diferentes operações
        
        Args:
            node: Nó atual
            start: Início do intervalo do nó
            end: Fim do intervalo do nó
            left: Início do intervalo query
            right: Fim do intervalo query
            operation: 'sum', 'min', ou 'max'
        
        Returns:
            int: Resultado da query
        
        TODO: Implementar lógica genérica
        """
        pass
    
    def _update_range(self, node, start, end, index, value):
        """
        Update recursivo
        
        Args:
            node: Nó atual
            start: Início do intervalo
            end: Fim do intervalo
            index: Índice a atualizar
            value: Novo valor
        
        TODO: Implementar update recursivo
        """
        pass
    
    def __str__(self):
        """
        Representação do segment tree
        
        Returns:
            str: Segment tree formatado
        """
        pass