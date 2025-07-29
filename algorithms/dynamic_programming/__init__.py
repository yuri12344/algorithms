"""
Programação Dinâmica Completa - Algoritmos FAANG

Todos os algoritmos clássicos de DP implementados do zero
Usando apenas suas próprias estruturas de dados

FAANG DP Coverage:
- Knapsack variants (0/1, unbounded, fractional)
- LCS/LIS variants
- Edit distance problems
- Stock trading problems
- House robber patterns
- String DP problems
- Advanced optimizations

Módulos:
- knapsack: Todos os problemas de mochila
- lcs: Longest Common Subsequence e variações
- subset_sum: Subset sum problems
- matrix_chain: Matrix multiplication optimization
- stock_problems: Stock trading DP
- edit_distance: String alignment problems
- house_robber: House robber pattern
- dp_patterns: Common DP patterns
"""

from .knapsack import Knapsack
from .lcs import LongestCommonSubsequence
from .subset_sum import SubsetSum
from .matrix_chain import MatrixChainMultiplication
from .stock_problems import StockProblems
from .edit_distance import EditDistance
from .house_robber import HouseRobber
from .dp_patterns import DPPatterns

__all__ = [
    'Knapsack',                    # Problemas de mochila
    'LongestCommonSubsequence',    # LCS e variações
    'SubsetSum',                   # Subset sum problems
    'MatrixChainMultiplication',   # Multiplicação de matrizes
    'StockProblems',              # Problemas de ações
    'EditDistance',               # Distância de edição
    'HouseRobber',                # Padrão house robber
    'DPPatterns'                  # Padrões DP
]