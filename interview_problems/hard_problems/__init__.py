"""
Problemas Hard FAANG - Desafiadores

Problemas avançados para dominar entrevistas:
- Dynamic Programming complexo
- Graph algorithms avançados
- System design problems
- Advanced data structures

Complexidade: O(n log n) a O(n³)
Tempo estimado: 60-120 minutos cada
"""

from .dp_hard import DynamicProgrammingHard
from .graph_hard import GraphHard
from .system_design_hard import SystemDesignHard
from .advanced_ds import AdvancedDataStructures

__all__ = [
    'DynamicProgrammingHard', 'GraphHard', 
    'SystemDesignHard', 'AdvancedDataStructures'
]

# Lista de problemas hard mais frequentes
HARD_PROBLEMS = {
    'dynamic_programming': [
        'Regular Expression Matching',
        'Edit Distance',
        'Word Ladder II',
        'Longest Increasing Path',
        'Cherry Pickup',
        'Optimal Account Balancing'
    ],
    'graphs': [
        'Word Ladder II',
        'Course Schedule III',
        'Alien Dictionary',
        'Critical Connections',
        'Minimum Cost to Make Valid Path',
        'Redundant Connection'
    ],
    'system_design': [
        'Design LRU Cache',
        'Design Twitter',
        'Design Snake Game',
        'Design Hit Counter',
        'Design Underground System',
        'Design Phone Directory'
    ],
    'advanced': [
        'Serialize and Deserialize N-ary Tree',
        'Range Sum Query 2D - Mutable',
        'Count of Smaller Numbers After Self',
        'Max Sum of Rectangle No Larger Than K',
        'Longest Valid Parentheses'
    ]
}