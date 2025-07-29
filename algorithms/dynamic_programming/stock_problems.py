"""
Stock Trading Problems - Programação Dinâmica

Todos os problemas clássicos de trading de ações
Implementados do zero com suas estruturas

FAANG Coverage:
- Best Time to Buy and Sell Stock I-IV
- Cooldown period
- Transaction fees
- Multiple transactions
"""

class StockProblems:
    """
    Problemas de trading de ações com DP
    
    TODO: Implemente todos os variantes
    """
    
    @staticmethod
    def best_time_to_buy_sell_stock_once(prices):
        """
        Best Time to Buy and Sell Stock I - Uma transação
        
        TODO: Single pass com tracking de mínimo
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Amazon, Facebook question
        
        Ex: [7,1,5,3,6,4] → 5 (compra 1, venda 6)
        """
        pass
    
    @staticmethod
    def best_time_to_buy_sell_stock_multiple(prices):
        """
        Best Time to Buy and Sell Stock II - Múltiplas transações
        
        TODO: Somar todos os picos
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Google, Apple question
        """
        pass
    
    @staticmethod
    def best_time_to_buy_sell_stock_with_cooldown(prices):
        """
        Best Time to Buy and Sell Stock with Cooldown
        
        TODO: DP com estados: hold, sold, cooldown
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Facebook, Microsoft question
        """
        pass
    
    @staticmethod
    def best_time_to_buy_sell_stock_with_fee(prices, fee):
        """
        Best Time to Buy and Sell Stock with Transaction Fee
        
        TODO: DP com subtração de taxa
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Amazon, Google question
        """
        pass
    
    @staticmethod
    def best_time_to_buy_sell_stock_iii(prices):
        """
        Best Time to Buy and Sell Stock III - Máximo 2 transações
        
        TODO: DP com 4 estados
        
        Complexidade: O(n) time, O(1) space
        
        FAANG: Hard Google question
        """
        pass