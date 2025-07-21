"""
CircularList - Lista Circular

A diferença é que o último aponta para o primeiro!
Útil para: filas circulares, round-robin, buffers
"""

from .linked_list import Node, LinkedList

class CircularList(LinkedList):
    """
    Lista Circular Simplesmente Encadeada
    
    Características especiais:
    - Último nó aponta para o primeiro
    - Não tem "None" no final
    - Cuidado com loops infinitos!
    
    TODO: Implemente com atenção aos loops
    """
    
    def __init__(self):
        """
        TODO: Inicialize circular list
        """
        super().__init__()
    
    def append(self, data):
        """
        TODO: Adicione no final (que aponta para o início)
        """
        pass
    
    def prepend(self, data):
        """
        TODO: Adicione no início (cuidado com o último)
        """
        pass
    
    def is_empty(self):
        """
        TODO: Lista vazia é quando head é None
        """
        pass
    
    def delete_first(self):
        """
        TODO: Remova primeiro elemento
        Ajuste o último para apontar para novo primeiro
        """
        pass
    
    def delete_last(self):
        """
        TODO: Remova último elemento
        O novo último deve apontar para o primeiro
        """
        pass
    
    def split_at(self, index):
        """
        DESAFIO: Divida a lista circular em duas
        Retorne nova lista com elementos a partir do index
        """
        pass
    
    def josephus_problem(self, k):
        """
        DESAFIO: Resolva o problema de Josephus
        Eliminar cada k-ésimo elemento até sobrar um
        Retorne a ordem de eliminação
        """
        pass
    
    def rotate(self, steps):
        """
        TODO: Rotacione a lista 'steps' posições
        Ex: rotate(1) em [1,2,3] vira [2,3,1]
        """
        pass
    
    def __str__(self):
        """
        TODO: Mostre como circular: "1 -> 2 -> 3 -> 1..."
        Cuidado para não entrar em loop infinito!
        """
        pass