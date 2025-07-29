"""
Edit Distance and String Alignment - Programação Dinâmica

Todos os problemas de distância de edição e alinhamento de strings
Implementados do zero com suas estruturas

FAANG Coverage:
- Levenshtein distance
- Hamming distance
- Longest common substring
- String alignment problems
"""

class EditDistance:
    """
    Distância de edição e problemas relacionados
    
    TODO: Implemente todos os algoritmos clássicos
    """
    
    @staticmethod
    def edit_distance(word1, word2):
        """
        Edit Distance - Distância de Levenshtein
        
        TODO: Implemente DP clássico
        
        Complexidade: O(m*n) time, O(m*n) space
        
        FAANG: Google, Facebook hard question
        
        Ex: "horse", "ros" → 3
        """
        pass
    
    @staticmethod
    def edit_distance_space_optimized(word1, word2):
        """
        Edit Distance com otimização de espaço
        
        TODO: Reduzir espaço para O(min(m,n))
        
        Complexidade: O(m*n) time, O(min(m,n)) space
        
        FAANG: Advanced optimization technique
        """
        pass
    
    @staticmethod
    def one_edit_distance(s, t):
        """
        One Edit Distance - Verificar se está a uma edição de distância
        
        TODO: Verificar se diff <= 1
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Amazon, Microsoft question
        """
        pass
    
    @staticmethod
    def hamming_distance(s1, s2):
        """
        Hamming Distance - Contar diferenças em strings de mesmo tamanho
        
        TODO: Contar caracteres diferentes
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Basic string comparison
        """
        pass
    
    @staticmethod
    def longest_common_subsequence_with_alignment(text1, text2):
        """
        LCS com alinhamento - Retornar a sequência alinhada
        
        TODO: Reconstruir a subsequência alinhada
        
        Complexidade: O(m*n) time, O(m*n) space
        
        FAANG: Bioinformatics application
        """
        pass