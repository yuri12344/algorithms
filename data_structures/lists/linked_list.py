"""
LinkedList - Lista Simplesmente Encadeada

DESAFIO: Implemente TODOS os métodos marcados com TODO
Não use código pronto, pense na lógica!
"""

class Node:
    """
    Nó simples para lista encadeada
    
    TODO: Implemente __init__ e __repr__
    """
    def __init__(self, data):
        # TODO: Inicialize data e next
        pass
    
    def __repr__(self):
        # TODO: Retorne string representando o nó
        pass

class LinkedList:
    """
    Lista Simplesmente Encadeada
    
    Operações básicas que você precisa implementar:
    - Inserção no início/fim/meio
    - Remoção por valor/posição
    - Busca
    - Tamanho
    - Impressão
    """
    
    def __init__(self):
        """
        TODO: Inicialize a lista vazia
        Dica: self.head = None
        """
        pass
    
    def __len__(self):
        """
        TODO: Retorne o número de elementos
        Dica: Percorra a lista contando
        """
        pass
    
    def __str__(self):
        """
        TODO: Retorne string bonita: "1 -> 2 -> 3 -> None"
        """
        pass
    
    def is_empty(self):
        """
        TODO: Retorne True se lista vazia
        """
        pass
    
    def append(self, data):
        """
        TODO: Adicione elemento no FINAL
        Complexidade alvo: O(n)
        """
        pass
    
    def prepend(self, data):
        """
        TODO: Adicione elemento no INÍCIO
        Complexidade alvo: O(1)
        """
        pass
    
    def insert_at(self, index, data):
        """
        TODO: Insira elemento na posição específica
        Dica: Trate casos especiais (início, fim, fora dos limites)
        """
        pass
    
    def find(self, data):
        """
        TODO: Retorne True se elemento existe
        """
        pass
    
    def get_at(self, index):
        """
        TODO: Retorne elemento na posição index
        Trate IndexError se fora dos limites
        """
        pass
    
    def delete_first(self):
        """
        TODO: Remova primeiro elemento
        Retorne o elemento removido
        Trate lista vazia
        """
        pass
    
    def delete_last(self):
        """
        TODO: Remova último elemento
        Retorne o elemento removido
        Trate lista vazia
        """
        pass
    
    def delete_value(self, data):
        """
        TODO: Remova primeira ocorrência do valor
        Retorne True se removeu, False se não encontrou
        """
        pass
    
    def reverse(self):
        """
        TODO: Inverta a ordem dos elementos
        Dica: Use três ponteiros ou recursão
        """
        pass
    
    def get_middle(self):
        """
        TODO: Retorne o elemento do meio
        Dica: Use slow/fast pointers
        """
        pass
    
    def has_cycle(self):
        """
        DESAFIO EXTRA: Detecte se tem ciclo (Floyd's algorithm)
        """
        pass