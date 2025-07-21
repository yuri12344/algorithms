"""
DoublyLinkedList - Lista Duplamente Encadeada

Agora você vai implementar uma lista que tem ponteiros para frente E para trás!

DESAFIO: Implemente os métodos herdados e os novos específicos
"""

from .linked_list import Node as SimpleNode, LinkedList

class Node(SimpleNode):
    """
    Nó duplo - tem next (próximo) e prev (anterior)
    
    TODO: Estenda o Node simples para incluir prev
    """
    def __init__(self, data):
        super().__init__(data)
        # TODO: Adicione o ponteiro prev
        pass
    
    def __repr__(self):
        # TODO: Mostre também o prev (opcional)
        pass

class DoublyLinkedList(LinkedList):
    """
    Lista Duplamente Encadeada
    
    Vantagens sobre a simples:
    - Pode andar para trás
    - Removeção do final é O(1) se tiver tail
    - Mais flexível para algumas operações
    
    TODO: Implemente os métodos específicos dessa estrutura
    """
    
    def __init__(self):
        """
        TODO: Inicialize com head e tail
        Dica: tail é o último elemento
        """
        super().__init__()
        # TODO: Adicione self.tail = None
        pass
    
    def append(self, data):
        """
        TODO: Adicione no final com tail
        Agora pode ser O(1)!
        """
        pass
    
    def prepend(self, data):
        """
        TODO: Adicione no início ajustando ponteiros duplos
        """
        pass
    
    def delete_last(self):
        """
        TODO: Remova último usando tail
        Agora pode ser O(1)!
        """
        pass
    
    def insert_before(self, node_data, new_data):
        """
        TODO: Insira novo elemento ANTES de um valor existente
        Dica: Precisa ajustar 4 ponteiros!
        """
        pass
    
    def insert_after(self, node_data, new_data):
        """
        TODO: Insira novo elemento DEPOIS de um valor existente
        """
        pass
    
    def reverse(self):
        """
        TODO: Inverta a lista aproveitando os ponteiros duplos
        Dica: Troque next e prev de cada nó
        """
        pass
    
    def traverse_backward(self):
        """
        TODO: Percorra da direita para esquerda
        Retorne lista com elementos em ordem reversa
        """
        pass
    
    def is_palindrome(self):
        """
        DESAFIO: Verifique se a lista é palíndromo
        Dica: Compare da esquerda e direita simultaneamente
        """
        pass