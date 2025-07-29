"""
Binary Tree Implementation - Do Zero!

Estrutura fundamental para todas as árvores.
Todos os métodos devem ser implementados do zero.
"""

class TreeNode:
    """
    Nó de árvore binária
    
    TODO: Implementar construtor e propriedades
    """
    
    def __init__(self, value):
        """
        Inicializa um nó com valor e filhos None
        
        Args:
            value: Valor armazenado no nó
        
        TODO:
        - self.value = value
        - self.left = None
        - self.right = None
        """
        pass
    
    def __repr__(self):
        """
        Representação string do nó
        
        Returns:
            str: "Node(value)"
        
        TODO: Retornar string formatada
        """
        pass


class BinaryTree:
    """
    Árvore Binária - estrutura fundamental
    
    Métodos essenciais para FAANG:
    - Traversals (pre, in, post, level)
    - Properties (height, size, balanced)
    - Serialization/Deserialization
    """
    
    def __init__(self):
        """
        Inicializa árvore vazia
        
        TODO:
        - self.root = None
        - self._size = 0
        """
        pass
    
    def insert_level_order(self, values):
        """
        Insere valores em ordem de nível (BFS)
        
        Args:
            values: Lista de valores para inserir
        
        TODO:
        - Usar sua Queue implementada
        - Criar nós na ordem correta
        - Atualizar size
        
        Example:
            tree = BinaryTree()
            tree.insert_level_order([1, 2, 3, 4, 5])
            # Cria:    1
            #        /   \
            #       2     3
            #      / \
            #     4   5
        """
        pass
    
    def preorder_traversal(self):
        """
        Pre-order traversal: root -> left -> right
        
        Returns:
            list: Valores em ordem pre-order
        
        TODO:
        - Implementar recursivamente
        - Ou iterativamente com sua Stack
        
        Example:
            tree.preorder_traversal()  # [1, 2, 4, 5, 3]
        """
        pass
    
    def inorder_traversal(self):
        """
        In-order traversal: left -> root -> right
        
        Returns:
            list: Valores em ordem in-order
        
        TODO: Implementar traversal
        """
        pass
    
    def postorder_traversal(self):
        """
        Post-order traversal: left -> right -> root
        
        Returns:
            list: Valores em ordem post-order
        
        TODO: Implementar traversal
        """
        pass
    
    def level_order_traversal(self):
        """
        Level-order traversal (BFS)
        
        Returns:
            list: Valores por nível
        
        TODO:
        - Usar sua Queue implementada
        - Visitar nível por nível
        """
        pass
    
    def height(self):
        """
        Altura da árvore
        
        Returns:
            int: Altura (raiz = 0)
        
        TODO:
        - Calcular recursivamente
        - Árvore vazia = -1
        """
        pass
    
    def size(self):
        """
        Número de nós na árvore
        
        Returns:
            int: Quantidade de nós
        
        TODO: Retornar tamanho armazenado
        """
        pass
    
    def is_empty(self):
        """
        Verifica se árvore está vazia
        
        Returns:
            bool: True se vazia
        
        TODO: Implementar verificação
        """
        pass
    
    def find(self, value):
        """
        Busca um valor na árvore
        
        Args:
            value: Valor a buscar
        
        Returns:
            TreeNode: Nó encontrado ou None
        
        TODO:
        - Usar BFS ou DFS
        - Retornar nó ou None
        """
        pass
    
    def is_balanced(self):
        """
        Verifica se árvore está balanceada
        
        Returns:
            bool: True se balanceada
        
        TODO:
        - Diferença de altura <= 1 para todos nós
        - Implementar recursivamente
        """
        pass
    
    def diameter(self):
        """
        Diâmetro da árvore (maior caminho entre folhas)
        
        Returns:
            int: Número de arestas no maior caminho
        
        TODO: Implementar com recursão
        """
        pass
    
    def serialize(self):
        """
        Serializa árvore para string (pre-order)
        
        Returns:
            str: Representação serializada
        
        TODO:
        - Usar pre-order traversal
        - Usar 'None' para nós vazios
        """
        pass
    
    def deserialize(self, data):
        """
        Desserializa string para árvore
        
        Args:
            data: String serializada
        
        TODO:
        - Reconstruir árvore da string
        - Usar index iterativo
        """
        pass
    
    def __len__(self):
        """
        Tamanho da árvore (mágico Python)
        
        Returns:
            int: Número de nós
        """
        pass
    
    def __str__(self):
        """
        Representação visual da árvore
        
        Returns:
            str: Árvore formatada
        
        TODO: Implementar formatação bonita
        """
        pass


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree - ordenada e eficiente
    
    Propriedade BST: left < root < right
    
    Métodos FAANG essenciais:
    - Insert/Delete O(log n)
    - Search O(log n)
    - Validation
    - Kth smallest/largest
    - Range queries
    """
    
    def insert(self, value):
        """
        Insere valor mantendo propriedade BST
        
        Args:
            value: Valor a inserir
        
        TODO:
        - Encontrar posição correta
        - Criar novo nó
        - Manter propriedade BST
        
        Time: O(log n) avg, O(n) worst
        """
        pass
    
    def delete(self, value):
        """
        Remove valor da árvore
        
        Args:
            value: Valor a remover
        
        Returns:
            bool: True se removido
        
        TODO:
        - 3 casos: folha, 1 filho, 2 filhos
        - Atualizar ponteiros
        - Manter propriedade BST
        """
        pass
    
    def search(self, value):
        """
        Busca eficiente em BST
        
        Args:
            value: Valor a buscar
        
        Returns:
            TreeNode: Nó encontrado ou None
        
        TODO:
        - Comparar e descer recursivamente
        - left < value < right
        """
        pass
    
    def find_min(self):
        """
        Menor valor na BST
        
        Returns:
            TreeNode: Nó com menor valor
        
        TODO: Descer sempre à esquerda
        """
        pass
    
    def find_max(self):
        """
        Maior valor na BST
        
        Returns:
            TreeNode: Nó com maior valor
        
        TODO: Descer sempre à direita
        """
        pass
    
    def is_valid_bst(self):
        """
        Valida se árvore mantém propriedade BST
        
        Returns:
            bool: True se válida
        
        TODO:
        - Verificar para todos nós
        - left < node < right
        """
        pass
    
    def kth_smallest(self, k):
        """
        K-ésimo menor elemento
        
        Args:
            k: Posição (1-indexed)
        
        Returns:
            int: Valor do k-ésimo menor
        
        TODO:
        - In-order traversal iterativo
        - Parar após k elementos
        """
        pass
    
    def range_sum(self, low, high):
        """
        Soma de valores entre low e high
        
        Args:
            low: Valor mínimo
            high: Valor máximo
        
        Returns:
            int: Soma dos valores no range
        
        TODO:
        - Busca otimizada
        - Somar nós no range
        """
        pass
    
    def floor(self, value):
        """
        Maior valor <= value
        
        Args:
            value: Valor de referência
        
        Returns:
            int: Floor value ou None
        
        TODO: Implementar busca
        """
        pass
    
    def ceiling(self, value):
        """
        Menor valor >= value
        
        Args:
            value: Valor de referência
        
        Returns:
            int: Ceiling value ou None
        
        TODO: Implementar busca
        """
        pass