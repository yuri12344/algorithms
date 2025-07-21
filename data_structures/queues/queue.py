"""
Queue - Fila FIFO

Como Stack, mas remove do início (FIFO)

Implementações possíveis:
1. LinkedList (recomendado)
2. Dois stacks (tricky)
3. Array circular

TODO: Implemente sua própria versão!
"""

from ..lists.linked_list import LinkedList

class Queue:
    """
    Fila FIFO (First In, First Out)
    
    Operações principais:
    - enqueue: entrar na fila (final)
    - dequeue: sair da fila (início)
    - front: ver primeiro sem remover
    - rear: ver último sem remover
    
    TODO: Use LinkedList para implementar!
    """
    
    def __init__(self):
        """
        TODO: Inicialize fila vazia
        """
        pass
    
    def enqueue(self, item):
        """
        TODO: Adicione elemento no FINAL
        Complexidade alvo: O(1)
        """
        pass
    
    def dequeue(self):
        """
        TODO: Remova e retorne do INÍCIO
        Trate caso vazio (IndexError)
        Complexidade alvo: O(1)
        """
        pass
    
    def front(self):
        """
        TODO: Veja primeiro elemento sem remover
        """
        pass
    
    def rear(self):
        """
        TODO: Veja último elemento sem remover
        """
        pass
    
    def is_empty(self):
        """
        TODO: Verifique se fila está vazia
        """
        pass
    
    def size(self):
        """
        TODO: Retorne número de elementos
        """
        pass
    
    def __len__(self):
        """
        TODO: Permita len(queue)
        """
        pass
    
    def __str__(self):
        """
        TODO: Mostre fila da frente para trás
        Ex: "Front -> 1 2 3 <- Rear"
        """
        pass
    
    def clear(self):
        """
        TODO: Esvazie a fila
        """
        pass
    
    def to_list(self):
        """
        DESAFIO: Converta para lista Python
        Mantenha ordem FIFO
        """
        pass