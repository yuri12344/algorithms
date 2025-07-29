"""
Problemas Medium FAANG - Avançados

Problemas intermediários que combinam estruturas:
- Trees e traversals
- Graphs BFS/DFS
- Hash Tables complexos
- Two pointers avançados

Complexidade: O(n log n) ou O(n²)
Tempo estimado: 30-60 minutos cada
"""

from .trees_medium import TreesMedium
from .graphs_medium import GraphsMedium
from .hash_tables_medium import HashTablesMedium
from .two_pointers_medium import TwoPointersMedium
from .dynamic_programming_medium import DynamicProgrammingMedium

__all__ = [
    'TreesMedium', 'GraphsMedium', 'HashTablesMedium', 
    'TwoPointersMedium', 'DynamicProgrammingMedium'
]

# Lista de problemas medium mais frequentes
MEDIUM_PROBLEMS = {
    'trees': [
        'Binary Tree Level Order Traversal',
        'Validate Binary Search Tree',
        'Lowest Common Ancestor',
        'Binary Tree Maximum Path Sum',
        'Serialize and Deserialize Binary Tree',
        'Path Sum III'
    ],
    'graphs': [
        'Number of Islands',
        'Course Schedule',
        'Word Ladder',
        'Clone Graph',
        'Pacific Atlantic Water Flow',
        'Alien Dictionary'
    ],
    'hash_tables': [
        'Group Anagrams',
        'Top K Frequent Elements',
        'Longest Substring Without Repeating',
        'LRU Cache',
        'Design Twitter',
        'Valid Sudoku'
    ],
    'two_pointers': [
        '3Sum',
        'Container With Most Water',
        'Trapping Rain Water',
        'Sort Colors',
        'Find All Anagrams'
    ]
}