"""
Algoritmos de Busca e Pattern Matching

Algoritmos essenciais para encontrar elementos e padrões
Todos implementados usando suas próprias estruturas de dados

FAANG Coverage:
- Binary Search variants
- Hash-based search
- String matching algorithms
- Two pointers technique
- Sliding window patterns
"""

from .binary_search import BinarySearch
from .linear_search import LinearSearch
from .string_matching import StringMatching
from .two_pointers import TwoPointers
from .sliding_window import SlidingWindow

__all__ = ['BinarySearch', 'LinearSearch', 'StringMatching', 'TwoPointers', 'SlidingWindow']