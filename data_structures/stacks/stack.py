"""
Stack - Pilha LIFO

Pode ser implementada usando:
1. Lista encadeada (recomendado)
2. Array dinâmico
3. Lista Python (para testes)

TODO: Escolha sua implementação e complete os métodos
"""

from ..lists.linked_list import LinkedList

class Stack:
    """
    Pilha LIFO (Last In, First Out)
    
    Operações principais:
    - push: empilhar no topo
    - pop: desempilhar do topo
    - peek: ver topo sem remover
    - is_empty: verificar se vazia
    
    TODO: Implemente usando LinkedList!
    """
    
    def __init__(self):
        """
        TODO: Inicialize stack vazia
        Dica: Use sua LinkedList ou crie uma nova estrutura
        """
        pass
    
    def push(self, item):
        """
        TODO: Adicione elemento no topo
        Complexidade alvo: O(1)
        """
        pass
    
    def pop(self):
        """
        TODO: Remova e retorne elemento do topo
        Trate caso vazio (IndexError)
        Complexidade alvo: O(1)
        """
        pass
    
    def peek(self):
        """
        TODO: Retorne elemento do topo sem remover
        Trate caso vazio (IndexError)
        """
        pass
    
    def is_empty(self):
        """
        TODO: Retorne True se vazia
        """
        pass
    
    def size(self):
        """
        TODO: Retorne número de elementos
        """
        pass
    
    def __len__(self):
        """
        TODO: Permita len(stack)
        """
        pass
    
    def __str__(self):
        """
        TODO: Mostre stack de cima para baixo
        Ex: "Top: 3 2 1"
        """
        pass
    
    def clear(self):
        """
        TODO: Esvazie a stack
        """
        pass
    
    def to_list(self):
        """
        DESAFIO: Converta stack para lista Python
        Mantenha ordem (topo primeiro)
        """
        pass
    
    def reverse_stack(self):
        """
        DESAFIO: Inverta ordem dos elementos
        Usando apenas uma stack auxiliar
        """
        pass