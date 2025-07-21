"""
Problemas de Entrevista FAANG - Coleção Completa

100+ problemas clássicos organizados por dificuldade
Todos implementados usando suas próprias estruturas

Categorias:
- Easy: Arrays, Strings, Linked Lists
- Medium: Trees, Graphs, DP, Two Pointers
- Hard: Advanced algorithms, System design

Includes:
- Problem statements
- Constraints
- Examples
- Hints
- Solutions structure
"""

from .easy_problems import EasyProblems
from .medium_problems import MediumProblems
from .hard_problems import HardProblems
from .leetcode_hot100 import LeetCodeHot100
from .company_specific import (
    GoogleProblems, AmazonProblems, FacebookProblems,
    AppleProblems, MicrosoftProblems, NetflixProblems
)

__all__ = [
    'EasyProblems', 'MediumProblems', 'HardProblems',
    'LeetCodeHot100', 'GoogleProblems', 'AmazonProblems',
    'FacebookProblems', 'AppleProblems', 'MicrosoftProblems',
    'NetflixProblems'
]

# Perguntas mais frequentes FAANG
TOP_FAANG_QUESTIONS = {
    'arrays': [
        'Two Sum', 'Best Time to Buy and Sell Stock', 'Contains Duplicate',
        'Product of Array Except Self', 'Maximum Subarray', 'Find All Numbers Disappeared'
    ],
    'strings': [
        'Valid Anagram', 'Group Anagrams', 'Longest Substring Without Repeating',
        'Longest Palindromic Substring', 'String to Integer (atoi)', 'Implement strStr()'
    ],
    'linked_lists': [
        'Reverse Linked List', 'Merge Two Sorted Lists', 'Linked List Cycle',
        'Remove Nth Node From End', 'Palindrome Linked List', 'Intersection of Two Lists'
    ],
    'trees': [
        'Maximum Depth of Binary Tree', 'Validate Binary Search Tree', 'Binary Tree Level Order',
        'Lowest Common Ancestor', 'Binary Tree Maximum Path Sum', 'Serialize and Deserialize'
    ],
    'graphs': [
        'Number of Islands', 'Clone Graph', 'Course Schedule', 'Word Ladder',
        'Pacific Atlantic Water Flow', 'Alien Dictionary'
    ],
    'dynamic_programming': [
        'Climbing Stairs', 'House Robber', 'Coin Change', 'Longest Increasing Subsequence',
        'Edit Distance', 'Word Break', 'Decode Ways', 'Unique Paths'
    ],
    'system_design': [
        'LRU Cache', 'Design Twitter', 'Design Hit Counter', 'Design Phone Directory',
        'Design Snake Game', 'Design Tic-Tac-Toe', 'Design Underground System'
    ]
}