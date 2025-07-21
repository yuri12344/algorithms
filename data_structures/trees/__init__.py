"""
Árvores - Estruturas de Dados Essenciais

Árvores binárias, AVL, Red-Black, B-Trees, e mais
Todas implementadas do zero usando suas próprias estruturas

FAANG Tree Coverage:
- Binary Tree (traversals, properties)
- Binary Search Tree (insert, delete, search)
- AVL Tree (self-balancing)
- Heap (min/max)
- Trie (prefix tree)
- Segment Tree (range queries)
"""

from .binary_tree import BinaryTree, BinarySearchTree
from .avl_tree import AVLTree
from .heap import MinHeap, MaxHeap
from .trie import Trie
from .segment_tree import SegmentTree
from .red_black_tree import RedBlackTree

__all__ = [
    'BinaryTree', 'BinarySearchTree', 'AVLTree',
    'MinHeap', 'MaxHeap', 'Trie', 'SegmentTree', 'RedBlackTree'
]