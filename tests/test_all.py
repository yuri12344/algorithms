"""
Testes para sua library de algoritmos

Cada teste vai FALHAR inicialmente
Implemente as estruturas até TODOS passarem!

Para rodar: python -m pytest tests/test_all.py -v
"""

import pytest
import sys
import os

# Adiciona o diretório raiz ao path para importar suas estruturas
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.lists import LinkedList, DoublyLinkedList, CircularList
from data_structures.stacks import Stack
from data_structures.queues import Queue, CircularQueue
from data_structures.hashing import HashTable, HashMap

# ===== TESTES LINKEDLIST =====

class TestLinkedList:
    def test_init(self):
        """Testa inicialização vazia"""
        ll = LinkedList()
        assert ll.is_empty()
        assert len(ll) == 0
    
    def test_append(self):
        """Testa adicionar elementos"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert len(ll) == 3
        assert str(ll) == "1 -> 2 -> 3 -> None"
    
    def test_prepend(self):
        """Testa adicionar no início"""
        ll = LinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        assert str(ll) == "1 -> 2 -> 3 -> None"
    
    def test_find(self):
        """Testa busca"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.find(2) == True
        assert ll.find(99) == False
    
    def test_delete_value(self):
        """Testa remoção por valor"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete_value(2)
        assert str(ll) == "1 -> 3 -> None"
        assert len(ll) == 2
    
    def test_reverse(self):
        """Testa reversão"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        assert str(ll) == "3 -> 2 -> 1 -> None"

# ===== TESTES DOUBLYLINKEDLIST =====

class TestDoublyLinkedList:
    def test_append_tail_efficiency(self):
        """Testa append O(1) com tail"""
        dll = DoublyLinkedList()
        for i in range(100):
            dll.append(i)
        assert len(dll) == 100
    
    def test_traverse_backward(self):
        """Testa percurso reverso"""
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        backward = dll.traverse_backward()
        assert backward == [3, 2, 1]
    
    def test_insert_before_after(self):
        """Testa inserção com ponteiros duplos"""
        dll = DoublyLinkedList()
        dll.append(2)
        dll.append(4)
        dll.insert_before(4, 3)
        dll.insert_after(2, 1)
        assert str(dll) == "1 -> 2 -> 3 -> 4 -> None"

# ===== TESTES CIRCULARLIST =====

class TestCircularList:
    def test_circular_append(self):
        """Testa append circular"""
        cl = CircularList()
        cl.append(1)
        cl.append(2)
        cl.append(3)
        assert len(cl) == 3
    
    def test_rotate(self):
        """Testa rotação"""
        cl = CircularList()
        cl.append(1)
        cl.append(2)
        cl.append(3)
        cl.rotate(1)
        # Depois de rodar 1 vez: 2, 3, 1
        # Implemente o teste quando completar rotate()
        pass
    
    def test_josephus(self):
        """Testa problema de Josephus"""
        cl = CircularList()
        for i in range(1, 6):
            cl.append(i)
        result = cl.josephus_problem(2)
        # Esperado: [2, 4, 1, 5, 3]
        assert result == [2, 4, 1, 5, 3]

# ===== TESTES STACK =====

class TestStack:
    def test_lifo_behavior(self):
        """Testa comportamento LIFO"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_peek(self):
        """Testa peek"""
        stack = Stack()
        stack.push(42)
        assert stack.peek() == 42
        assert len(stack) == 1
    
    def test_empty_pop_raises(self):
        """Testa erro ao desempilhar vazio"""
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

# ===== TESTES QUEUE =====

class TestQueue:
    def test_fifo_behavior(self):
        """Testa comportamento FIFO"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
    
    def test_front_rear(self):
        """Testa visualização elementos"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.front() == 1
        assert queue.rear() == 3

# ===== TESTES HASHTABLE =====

class TestHashTable:
    def test_basic_insert_get(self):
        """Testa inserção e recuperação"""
        ht = HashTable()
        ht.insert("nome", "Yuri")
        ht.insert("idade", 25)
        assert ht.get("nome") == "Yuri"
        assert ht.get("idade") == 25
    
    def test_key_not_found(self):
        """Testa erro chave não encontrada"""
        ht = HashTable()
        with pytest.raises(KeyError):
            ht.get("inexistente")
    
    def test_update_value(self):
        """Testa atualização de valor"""
        ht = HashTable()
        ht.insert("chave", "valor1")
        ht.insert("chave", "valor2")
        assert ht.get("chave") == "valor2"
    
    def test_collision_handling(self):
        """Testa tratamento de colisões"""
        ht = HashTable(initial_capacity=2)
        # Força colisões com strings que hash igual
        keys = ["Aa", "BB"]  # Estas colidem no Python
        for key in keys:
            ht.insert(key, f"valor_{key}")
        
        for key in keys:
            assert ht.get(key) == f"valor_{key}"

# ===== TESTES HASHMAP =====

class TestHashMap:
    def test_dict_like_behavior(self):
        """Testa interface de dicionário"""
        hm = HashMap()
        hm["nome"] = "Yuri"
        hm["idade"] = 25
        assert hm["nome"] == "Yuri"
        assert len(hm) == 2
        del hm["idade"]
        assert len(hm) == 1
    
    def test_keys_sorted(self):
        """Testa chaves ordenadas"""
        hm = HashMap()
        hm["zebra"] = 1
        hm["apple"] = 2
        hm["banana"] = 3
        sorted_keys = hm.keys_sorted()
        assert sorted_keys == ["apple", "banana", "zebra"]

# ===== INTEGRATION TESTS =====

class TestIntegration:
    def test_stack_with_linkedlist(self):
        """Testa Stack usando sua LinkedList"""
        # Implemente quando ambos estiverem prontos
        pass
    
    def test_hash_with_linkedlist_chaining(self):
        """Testa HashTable usando LinkedList para colisões"""
        # Implemente quando ambos estiverem prontos
        pass
    
    def test_data_flow(self):
        """Testa fluxo completo de dados"""
        # 1. Adicione dados ao HashTable
        # 2. Extraia para LinkedList
        # 3. Ordene com algoritmo
        # 4. Coloque de volta em Stack
        pass

if __name__ == "__main__":
    # Roda testes manualmente se quiser
    pytest.main([__file__, "-v"])