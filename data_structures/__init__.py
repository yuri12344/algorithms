"""
Minha Library Completa de Estruturas de Dados

Estruturas organizadas de forma modular para aprendizado progressivo
Todas implementadas do zero usando Python puro

Módulos:
- lists: LinkedList, DoublyLinkedList, CircularList
- stacks: Stack (LIFO)
- queues: Queue (FIFO), CircularQueue
- hashing: HashTable, HashMap
- trees: BinaryTree, BST, AVL, Heap, Trie
- graphs: Graph, DirectedGraph, WeightedGraph, DAG
"""

# Listas Encadeadas
from .lists import LinkedList, DoublyLinkedList, CircularList

# Pilhas e Filas
from .stacks import Stack
from .queues import Queue, CircularQueue

# Hashing
from .hashing import HashTable, HashMap

# Árvores
from .trees import BinaryTree, BinarySearchTree, AVLTree, MinHeap, MaxHeap, Trie

# Grafos
from .graphs import Graph, DirectedGraph, WeightedGraph, DAG

__all__ = [
    # Listas
    'LinkedList', 'DoublyLinkedList', 'CircularList',
    # Pilhas/Filas
    'Stack', 'Queue', 'CircularQueue',
    # Hashing
    'HashTable', 'HashMap',
    # Árvores
    'BinaryTree', 'BinarySearchTree', 'AVLTree', 'MinHeap', 'MaxHeap', 'Trie',
    # Grafos
    'Graph', 'DirectedGraph', 'WeightedGraph', 'DAG'
]