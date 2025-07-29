"""
Problemas Easy FAANG - Fundamentos

Problemas essenciais para começar:
- Arrays e Strings
- Linked Lists básicas
- Stacks e Queues
- Hash Tables simples

Complexidade: O(n) ou O(n log n)
Tempo estimado: 15-30 minutos cada
"""

from .arrays_strings import ArraysStrings
from .linked_lists_easy import LinkedListsEasy
from .stacks_queues_easy import StacksQueuesEasy
from .hash_tables_easy import HashTablesEasy

__all__ = [
    'ArraysStrings', 
    'LinkedListsEasy', 
    'StacksQueuesEasy', 
    'HashTablesEasy'
]

# Lista de problemas easy mais frequentes
EASY_PROBLEMS = {
    'arrays': [
        'Two Sum',
        'Valid Anagram',
        'Contains Duplicate',
        'Single Number',
        'Maximum Subarray',
        'Plus One',
        'Move Zeroes',
        'Best Time to Buy and Sell Stock'
    ],
    'strings': [
        'Valid Palindrome',
        'Valid Anagram',
        'First Unique Character',
        'Reverse String',
        'Reverse Vowels',
        'Valid Parentheses',
        'Implement strStr()',
        'Length of Last Word'
    ],
    'linked_lists': [
        'Reverse Linked List',
        'Merge Two Sorted Lists',
        'Linked List Cycle',
        'Intersection of Two Lists',
        'Remove Nth Node From End',
        'Palindrome Linked List'
    ],
    'stacks_queues': [
        'Valid Parentheses',
        'Min Stack',
        'Queue using Stacks',
        'Implement Stack using Queues',
        'Evaluate Reverse Polish Notation'
    ]
}