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

🎯 INSTRUÇÕES DE IMPLEMENTAÇÃO:

1. **Comece com BinaryTree** (1-2 semanas)
   - Implemente TreeNode primeiro
   - Depois traversals (pre, in, post, level)
   - Teste com exemplos simples

2. **BST - Binary Search Tree** (1-2 semanas)
   - Estende BinaryTree
   - Implementa insert/delete/search O(log n)
   - Valida propriedade BST

3. **AVL Tree** (2-3 semanas)
   - Estende BST com balanceamento
   - Implementa rotações (left, right)
   - Mantém fator de balanceamento

4. **Heaps** (1 semana)
   - MinHeap: menor elemento no topo
   - MaxHeap: maior elemento no topo
   - Usa arrays internos para eficiência

5. **Trie** (1 semana)
   - Para strings e prefixos
   - Útil para autocomplete

6. **Segment Tree** (2 semanas)
   - Queries de range O(log n)
   - Point updates O(log n)

7. **Red-Black Tree** (opcional, avançado)
   - Balanceamento complexo
   - Melhor para muitas inserções

📅 ORDEM RECOMENDADA:
BinaryTree → BST → AVL → Heaps → Trie → SegmentTree → RedBlackTree
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