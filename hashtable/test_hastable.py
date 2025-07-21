import unittest
from main import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        """Set up a new HashTable for each test."""
        self.hash_table = HashTable(5)
        self.person1 = {"yuri caetano": "CPF: 221.509.123-09"}
        self.person1_updated = {"yuri caetano": "CPF: 222.222.222.-59"}
        self.person2 = {'yuri caetano2': '119841981299'}

    def test_initialization(self):
        """Test if the hash table initializes correctly."""
        self.assertEqual(self.hash_table.size, 5)
        self.assertEqual(self.hash_table.slots, [[], [], [], [], []])

    def test_store_and_search(self):
        """Test storing a new item and searching for it."""
        self.hash_table.store(self.person1)
        self.assertEqual(self.hash_table.search("yuri caetano"), self.person1)
        self.assertIsNone(self.hash_table.search("non_existent_key"))

    def test_update(self):
        """Test updating an existing item."""
        self.hash_table.store(self.person1)
        self.hash_table.store(self.person1_updated)
        self.assertEqual(self.hash_table.search("yuri caetano"), self.person1_updated)

    def test_collision(self):
        """Test handling of items in same slot."""
        self.hash_table.store(self.person1)
        self.hash_table.store(self.person2)
        hash_val = self.hash_table.hash("yuri caetano")
        hash_val2 = self.hash_table.hash("yuri caetano2")
        
        # Check items are stored correctly whether same slot or different
        self.assertIsNotNone(self.hash_table.search("yuri caetano"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano2"))

    def test_delete(self):
        """Test deleting an item."""
        self.hash_table.store(self.person1)
        self.hash_table.delete("yuri caetano")
        self.assertIsNone(self.hash_table.search("yuri caetano"))

    def test_delete_with_multiple_items(self):
        """Test deleting an item when multiple items exist."""
        self.hash_table.store(self.person1)
        self.hash_table.store(self.person2)
        
        # Delete one of the items
        self.hash_table.delete("yuri caetano2")
        
        # Check that the deleted item is gone, but the other remains
        self.assertIsNone(self.hash_table.search("yuri caetano2"))
        self.assertEqual(self.hash_table.search("yuri caetano"), self.person1)

    def test_delete_non_existent(self):
        """Test that deleting a non-existent key does not raise an error."""
        self.hash_table.store(self.person1)
        try:
            self.hash_table.delete("non_existent_key")
        except Exception as e:
            self.fail(f"delete() raised {e.__class__.__name__} unexpectedly!")
        self.assertEqual(self.hash_table.search("yuri caetano"), self.person1)

    def test_multiple_items(self):
        """Test handling of multiple items."""
        person3 = {'yuri caetano3': '333333333'}
        person4 = {'yuri caetano4': '444444444'}
        
        self.hash_table.store(self.person1)
        self.hash_table.store(self.person2)
        self.hash_table.store(person3)
        self.hash_table.store(person4)
        
        # Test all items can be found
        self.assertIsNotNone(self.hash_table.search("yuri caetano"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano2"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano3"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano4"))
        
        # Test deleting works correctly
        self.hash_table.delete("yuri caetano2")
        self.assertIsNone(self.hash_table.search("yuri caetano2"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano3"))
        self.assertIsNotNone(self.hash_table.search("yuri caetano4"))

    def test_hash_distribution(self):
        """Test that hash function distributes values across slots."""
        items = [
            {"test1": "value1"},
            {"different": "value2"},
            {"completely": "value3"},
            {"random": "value4"},
            {"keys": "value5"}
        ]
        
        used_slots = set()
        for item in items:
            self.hash_table.store(item)
            key = list(item.keys())[0]
            used_slots.add(self.hash_table.hash(key))
        
        # Check that at least 3 different slots were used
        self.assertGreaterEqual(len(used_slots), 3)

    def test_overflow(self):
        """Test handling when adding more items than initial slots."""
        # Create a small hash table
        small_table = HashTable(2)
        
        # Try to add more items than slots
        items = [
            {"key1": "value1"},
            {"key2": "value2"},
            {"key3": "value3"},
            {"key4": "value4"}
        ]
        
        # Store all items
        for item in items:
            small_table.store(item)
            
        # Verify all items can still be found
        for item in items:
            key = list(item.keys())[0]
            self.assertEqual(small_table.search(key), item)

if __name__ == '__main__':
    unittest.main()
