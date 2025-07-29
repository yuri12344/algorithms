"""
Algoritmos de Ordenação sobre Estruturas de Dados

Todos os algoritmos são implementados sobre suas próprias estruturas:
- LinkedList: Merge Sort, Quick Sort
- Arrays: Quick Sort variants, Heap Sort
- Custom data structures

FAANG Interview Focus:
- Time/Space complexity analysis
- Stability
- In-place vs extra space
- Real-world applications
"""

from .linked_list_sorting import LinkedListSorting
from .array_sorting import ArraySorting
from .external_sorting import ExternalSorting
from .sorting_utils import SortingUtils

__all__ = ['LinkedListSorting', 'ArraySorting', 'ExternalSorting', 'SortingUtils']