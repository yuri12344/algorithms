"""
House Robber Problems - Programação Dinâmica

Padrão clássico de "house robber" com múltiplas variações
Implementado do zero com suas estruturas

FAANG Coverage:
- House Robber I-III
- House Robber with constraints
- Circular arrangement
- Binary tree version
"""

class HouseRobber:
    """
    Problemas do padrão "house robber"
    
    TODO: Implemente todas as variações clássicas
    """
    
    @staticmethod
    def house_robber_linear(nums):
        """
        House Robber I - Linha de casas
        
        TODO: DP clássico - não pode roubar casas adjacentes
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Amazon, Facebook, Google question
        
        Ex: [1,2,3,1] → 4 (rouba casa 1 e 3)
        """
        pass
    
    @staticmethod
    def house_robber_circular(nums):
        """
        House Robber II - Casas em círculo
        
        TODO: DP com restrição circular
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Hard Amazon, Google question
        """
        pass
    
    @staticmethod
    def house_robber_binary_tree(root):
        """
        House Robber III - Casas em árvore binária
        
        TODO: DP em árvore com post-order traversal
        
        Complexidade: O(n) time, O(h) space
        
        FAANG: Hard Google, Facebook question
        """
        pass
    
    @staticmethod
    def paint_house(costs):
        """
        Paint House - Pintar casas com cores diferentes
        
        TODO: DP com múltiplas cores
        
        Complexidade: O(n*k) time, O(k) space
        
        FAANG: Facebook, Microsoft question
        """
        pass
    
    @staticmethod
    def delete_and_earn(nums):
        """
        Delete and Earn - Deletar e ganhar pontos
        
        TODO: Transformar em house robber problem
        
        Complexidade: O(n + max(nums)) time, O(max(nums)) space
        
        FAANG: Amazon, Google question
        """
        pass