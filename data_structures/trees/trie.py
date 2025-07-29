"""
Trie (Prefix Tree) Implementation

Estrutura de dados para strings com operações prefixo
Essencial para autocomplete e busca por prefixo
"""


class TrieNode:
    """
    Nó da Trie
    
    TODO: Implementar estrutura do nó
    """
    
    def __init__(self):
        """
        Inicializa nó trie
        
        TODO:
        - self.children = {}  # char -> TrieNode
        - self.is_end_of_word = False
        - self.count = 0  # Conta palavras com este prefixo
        """
        pass
    
    def __repr__(self):
        """
        Representação string
        
        Returns:
            str: "TrieNode(is_word=X, count=Y)"
        """
        pass


class Trie:
    """
    Trie (Prefix Tree) para strings
    
    Métodos FAANG:
    - Insert O(word_length)
    - Search O(word_length)
    - Starts_with O(prefix_length)
    - Autocomplete
    """
    
    def __init__(self):
        """
        Inicializa trie vazia
        
        TODO:
        - self.root = TrieNode()
        """
        pass
    
    def insert(self, word):
        """
        Insere palavra na trie
        
        Args:
            word: Palavra a inserir
        
        TODO:
        - Percorrer caracteres
        - Criar nós se necessário
        - Marcar fim de palavra
        - Atualizar counts
        
        Time: O(word_length)
        """
        pass
    
    def search(self, word):
        """
        Busca palavra completa
        
        Args:
            word: Palavra a buscar
        
        Returns:
            bool: True se palavra existe
        
        TODO:
        - Percorrer caracteres
        - Verificar se é fim de palavra
        """
        pass
    
    def starts_with(self, prefix):
        """
        Verifica se prefixo existe
        
        Args:
            prefix: Prefixo a verificar
        
        Returns:
            bool: True se prefixo existe
        
        TODO:
        - Percorrer caracteres
        - Verificar se chega ao fim
        """
        pass
    
    def count_words_with_prefix(self, prefix):
        """
        Conta palavras com determinado prefixo
        
        Args:
            prefix: Prefixo a contar
        
        Returns:
            int: Número de palavras com prefixo
        
        TODO:
        - Percorrer até prefixo
        - Retornar count do último nó
        """
        pass
    
    def get_words_with_prefix(self, prefix):
        """
        Retorna todas palavras com prefixo
        
        Args:
            prefix: Prefixo para buscar
        
        Returns:
            list: Palavras com o prefixo
        
        TODO:
        - Percorrer até prefixo
        - DFS para encontrar todas palavras
        """
        pass
    
    def delete(self, word):
        """
        Remove palavra da trie
        
        Args:
            word: Palavra a remover
        
        Returns:
            bool: True se removida
        
        TODO:
        - Percorrer caracteres
        - Desmarcar fim de palavra
        - Remover nós sem filhos
        """
        pass
    
    def get_all_words(self):
        """
        Retorna todas palavras na trie
        
        Returns:
            list: Todas palavras
        
        TODO: DFS completa
        """
        pass
    
    def _dfs_words(self, node, prefix, words):
        """
        DFS para encontrar todas palavras
        
        Args:
            node: Nó atual
            prefix: Prefixo acumulado
            words: Lista para armazenar resultados
        
        TODO:
        - Adicionar palavra se for fim
        - Recursar em todos filhos
        """
        pass
    
    def longest_common_prefix(self):
        """
        Maior prefixo comum entre todas palavras
        
        Returns:
            str: Maior prefixo comum
        
        TODO:
        - Percorrer até encontrar ramificação
        - Ou até encontrar fim de palavra
        """
        pass
    
    def is_empty(self):
        """
        Verifica se trie está vazia
        
        Returns:
            bool: True se vazia
        """
        pass
    
    def __len__(self):
        """
        Número de palavras na trie
        
        Returns:
            int: Quantidade de palavras
        """
        pass
    
    def __str__(self):
        """
        Representação visual da trie
        
        Returns:
            str: Trie formatada
        """
        pass