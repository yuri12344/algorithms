"""
HashTable - Tabela Hash com tratamento de colisões

Usando SUAS listas encadeadas para resolver colisões!
Isso conecta tudo que você já implementou.
"""

from ..lists.linked_list import LinkedList

class HashTable:
    RE_HASH_FACTOR = 0.7
    RE_HASH_SIZE_MULTIPLY = 2
    PRIME_NUMBER = 31
    """
    Tabela Hash com chaining (listas encadeadas)
    
    Agora você vai conectar:
    1. Sua LinkedList (para resolver colisões)
    2. Hash functions (você já tem uma)
    3. Tudo junto em uma estrutura poderosa
    
    TODO: Implemente usando sua LinkedList!
    """
    
    def __init__(self, initial_capacity=16):
        """
        TODO: Inicialize tabela hash
        Dica: Array de LinkedLists (buckets)
        """
    

    def _hash(self, key: str):
        total = 0
        for char in key:
            total = (total * self.PRIME_NUMBER) + ord(char)
        return total % self.size
    
    def _resize(self):
        """
        DESAFIO: Redimensione quando fator de carga > 0.75
        Crie nova tabela maior e re-insira tudo
        """
        pass
    
    def insert(self, key, value):
        """
        TODO: Insira par chave-valor
        Use sua LinkedList para resolver colisões
        Trate chaves duplicadas (atualize valor)
        """
        pass
    
    def get(self, key):
        """
        TODO: Retorne valor pela chave
        Trate KeyError se não existir
        """
        pass
    
    def delete(self, key):
        """
        TODO: Remova chave-valor
        Retorne True se removeu, False se não encontrou
        """
        pass
    
    def contains(self, key):
        """
        TODO: Verifique se chave existe
        """
        pass
    
    def keys(self):
        """
        TODO: Retorne lista com todas as chaves
        Use suas estruturas para coletar!
        """
        pass
    
    def values(self):
        """
        TODO: Retorne lista com todos os valores
        """
        pass
    
    def items(self):
        """
        TODO: Retorne lista de tuplas (key, value)
        """
        pass
    
    def clear(self):
        """
        TODO: Esvazie a tabela hash
        """
        pass
    
    def __len__(self):
        """
        TODO: Total de elementos (não buckets)
        """
        pass
    
    def __str__(self):
        """
        TODO: Mostre estrutura bonita
        Ex: "0: [a:1, b:2]\n1: []\n2: [c:3]"
        """
        pass
    
    def load_factor(self):
        """
        DESAFIO: Calcule fator de carga
        elementos / buckets
        """
        pass
    
    def collision_count(self):
        """
        DESAFIO EXTRA: Conte número de colisões
        Buckets com mais de um elemento
        """
        pass

