"""
Programação Dinâmica - Algoritmos Essenciais

Todos os clássicos que caem em entrevistas FAANG
Implementados usando suas próprias estruturas de dados

FAANG DP Problems:
- Knapsack variants
- LCS variants  
- Subset sum
- Matrix chain multiplication
- House robber
- Stock problems
- Edit distance
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
    'Knapsack', 'LongestCommonSubsequence', 'SubsetSum',
    'MatrixChainMultiplication', 'StockProblems', 'EditDistance',
    'HouseRobber', 'DPPatterns'
]