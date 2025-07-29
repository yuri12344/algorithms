"""
Amazon Interview Problems - Problemas Específicos

Problemas que caem frequentemente em entrevistas da Amazon
Organizados por categoria e dificuldade
"""

from .amazon_arrays import AmazonArrays
from .amazon_strings import AmazonStrings
from .amazon_trees import AmazonTrees
from .amazon_dp import AmazonDP
from .amazon_system_design import AmazonSystemDesign

__all__ = [
    'AmazonArrays', 'AmazonStrings', 'AmazonTrees',
    'AmazonDP', 'AmazonSystemDesign'
]

# Problemas mais frequentes da Amazon
AMAZON_PROBLEMS = {
    'arrays': [
        'Two Sum',
        'Best Time to Buy and Sell Stock',
        'Contains Duplicate',
        'Product of Array Except Self',
        'Maximum Subarray'
    ],
    'strings': [
        'Valid Anagram',
        'Group Anagrams',
        'Valid Palindrome',
        'Longest Substring Without Repeating Characters',
        'Valid Parentheses'
    ],
    'trees': [
        'Maximum Depth of Binary Tree',
        'Validate Binary Search Tree',
        'Binary Tree Level Order Traversal',
        'Lowest Common Ancestor',
        'Path Sum'
    ],
    'dp': [
        'House Robber',
        'Coin Change',
        'Climbing Stairs',
        'Longest Increasing Subsequence',
        'Word Break'
    ],
    'system_design': [
        'Design LRU Cache',
        'Design Twitter',
        'Design Phone Directory',
        'Design Snake Game'
    ]
}