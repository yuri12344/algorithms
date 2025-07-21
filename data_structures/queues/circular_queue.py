"""
CircularQueue - Fila Circular

Usando sua CircularList para implementar uma fila circular!
Útil para buffers, round-robin, etc.
"""

from ..lists.circular_list import CircularList

class CircularQueue:
    """
    Fila Circular com tamanho fixo
    
    Quando cheia, próximo enqueue sobrescreve o mais antigo
    
    TODO: Implemente com CircularList!
    """
    
    def __init__(self, max_size):
        """
        TODO: Inicialize com tamanho máximo
        """
        pass
    
    def enqueue(self, item):
        """
        TODO: Adicione elemento
        Se cheia, sobrescreva o mais antigo (circular)
        """
        pass
    
    def dequeue(self):
        """
        TODO: Remova e retorne elemento mais antigo
        """
        pass
    
    def is_full(self):
        """
        TODO: Verifique se fila está cheia
        """
        pass
    
    def is_empty(self):
        """
        TODO: Verifique se fila está vazia
        """
        pass
    
    def peek(self):
        """
        TODO: Veja próximo a sair sem remover
        """
        pass
    
    def __len__(self):
        """
        TODO: Retorne elementos atuais (não max_size)
        """
        pass
    
    def __str__(self):
        """
        TODO: Mostre estado da fila circular
        Ex: "[1, 2, 3, _, _]" (onde _ é vazio)
        """
        pass