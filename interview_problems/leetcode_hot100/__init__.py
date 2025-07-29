"""
LeetCode Hot 100 - Problemas Mais Frequentes

Os 100 problemas mais importantes do LeetCode
Organizados por frequência em entrevistas FAANG

Categoria: Todos os níveis (Easy, Medium, Hard)
Fonte: LeetCode oficial rankings
"""

from .hot_100_list import Hot100List
from .problem_solutions import Hot100Solutions

__all__ = ['Hot100List', 'Hot100Solutions']

# LeetCode Hot 100 - Lista oficial
LEETCODE_HOT_100 = [
    # Arrays
    {'problem': 'Two Sum', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'Best Time to Buy and Sell Stock', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'Maximum Subarray', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'Product of Array Except Self', 'difficulty': 'Medium', 'frequency': '9/10'},
    {'problem': 'Find All Numbers Disappeared', 'difficulty': 'Easy', 'frequency': '8/10'},
    
    # Linked Lists
    {'problem': 'Reverse Linked List', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'Merge Two Sorted Lists', 'difficulty': 'Easy', 'frequency': '9/10'},
    {'problem': 'Linked List Cycle', 'difficulty': 'Easy', 'frequency': '9/10'},
    {'problem': 'Remove Nth Node From End', 'difficulty': 'Medium', 'frequency': '8/10'},
    
    # Trees
    {'problem': 'Maximum Depth of Binary Tree', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'Validate Binary Search Tree', 'difficulty': 'Medium', 'frequency': '10/10'},
    {'problem': 'Binary Tree Level Order Traversal', 'difficulty': 'Medium', 'frequency': '9/10'},
    {'problem': 'Lowest Common Ancestor', 'difficulty': 'Medium', 'frequency': '9/10'},
    
    # Dynamic Programming
    {'problem': 'Climbing Stairs', 'difficulty': 'Easy', 'frequency': '10/10'},
    {'problem': 'House Robber', 'difficulty': 'Medium', 'frequency': '9/10'},
    {'problem': 'Coin Change', 'difficulty': 'Medium', 'frequency': '9/10'},
    {'problem': 'Longest Increasing Subsequence', 'difficulty': 'Medium', 'frequency': '8/10'},
    
    # Graphs
    {'problem': 'Number of Islands', 'difficulty': 'Medium', 'frequency': '10/10'},
    {'problem': 'Course Schedule', 'difficulty': 'Medium', 'frequency': '9/10'},
    {'problem': 'Clone Graph', 'difficulty': 'Medium', 'frequency': '8/10'},
    
    # System Design
    {'problem': 'LRU Cache', 'difficulty': 'Medium', 'frequency': '10/10'},
    {'problem': 'Design Twitter', 'difficulty': 'Medium', 'frequency': '8/10'}
]