"""
HashMap - Mapa Hash Avançado

Versão mais completa que conecta várias estruturas:
- Usa HashTable como base
- Integra com suas listas para ordenação
- Adiciona funcionalidades extras

TODO: Construa em cima do HashTable!
"""

from .hash_table import HashTable

class HashMap:
    """
    HashMap avançado com funcionalidades extras
    
    Conecta:
    1. HashTable (base)
    2. LinkedList (para ordenação)
    3. Stack/Queue (para iteradores)
    
    TODO: Implemente funcionalidades que usam suas estruturas
    """
    
    def __init__(self):
        """
        TODO: Inicialize com HashTable interno
        """
        pass
    
    def __setitem__(self, key, value):
        """
        TODO: Permita map[key] = value
        """
        pass
    
    def __getitem__(self, key):
        """
        TODO: Permita map[key]
        """
        pass
    
    def __delitem__(self, key):
        """
        TODO: Permita del map[key]
        """
        pass
    
    def __contains__(self, key):
        """
        TODO: Permita key in map
        """
        pass
    
    def __len__(self):
        """
        TODO: Permita len(map)
        """
        pass
    
    def keys_sorted(self):
        """
        DESAFIO: Retorne chaves ordenadas usando suas estruturas
        Dica: Use LinkedList para implementar insertion sort
        """
        pass
    
    def values_sorted_by_key(self):
        """
        DESAFIO: Retorne valores ordenados pelas chaves
        """
        pass
    
    def reverse_iterator(self):
        """
        DESAFIO: Iterador reverso usando Stack
        """
        pass
    
    def frequency_map(self, data_list):
        """
        DESAFIO: Conte frequência de elementos
        Use para análise de dados
        """
        pass
    
    def group_by(self, key_func):
        """
        DESAFIO: Agrupe valores por função chave
        Ex: group_by(len) para strings
        """
        pass
    
    def merge_with(self, other_map):
        """
        DESAFIO: Una dois HashMaps
        Trate conflitos (último vence? soma valores?)
        """
        pass