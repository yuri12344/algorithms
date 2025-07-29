"""
Google Interview Problems - Problemas Específicos

Problemas que caem frequentemente em entrevistas da Google
Organizados por categoria e dificuldade
"""

from .google_arrays import GoogleArrays
from .google_strings import GoogleStrings
from .google_graphs import GoogleGraphs
from .google_dp import GoogleDP
from .google_system_design import GoogleSystemDesign

__all__ = [
    'GoogleArrays', 'GoogleStrings', 'GoogleGraphs',
    'GoogleDP', 'GoogleSystemDesign'
]

# Problemas mais frequentes da Google
GOOGLE_PROBLEMS = {
    'arrays': [
        'Find First and Last Position in Sorted Array',
        'Search in Rotated Sorted Array',
        'Product of Array Except Self',
        'Trapping Rain Water',
        'Container With Most Water'
    ],
    'strings': [
        'Longest Substring Without Repeating Characters',
        'Longest Palindromic Substring',
        'Regular Expression Matching',
        'Valid Palindrome',
        'Group Anagrams'
    ],
    'graphs': [
        'Number of Islands',
        'Course Schedule',
        'Clone Graph',
        'Word Ladder',
        'Pacific Atlantic Water Flow'
    ],
    'dp': [
        'Edit Distance',
        'Longest Increasing Subsequence',
        'Word Break',
        'Decode Ways',
        'Unique Paths'
    ],
    'system_design': [
        'Design LRU Cache',
        'Design Search Autocomplete System',
        'Design File System',
        'Design Hit Counter'
    ]
}