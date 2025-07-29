# Aux link: https://aistudio.google.com/prompts/1ScsJ1OxsGaL78c__F0y4xpGs1GfvFes5
import ipdb


class HashTable:
    RE_HASH_FACTOR = 0.7
    RE_HASH_SIZE_MULTIPLY = 2
    PRIME_NUMBER = 31

    def __init__(self, size=10):
        self.size = size
        self.slots = [[] for _ in range(self.size)]
        self.item_count = 0 

    def hash_problematic(self, key: str):
        """
        The problem with this is: The word TRASH will generate same hash to HSART increasing colisions
        First principle thinking: The position of each chr is ignored, lets supose if its not, it will improve  with less colisions
        """
        total = sum(ord(char) for char in key)
        return total % self.size

    def hash(self, key: str):
        total = 0

        for char in key:
            total = (total * self.PRIME_NUMBER) + ord(char)
        
        return total % self.size

    def _slot_available(self):
        return sum(1 for n in self.slots if not n)
    
    def _add(self, _hash, item):
        self.slots[_hash].append(item)
        self.item_count += 1

    def _update(self, _hash, key, item = None):
        for index, stored_object in enumerate(self.slots[_hash]):
            if key in stored_object:
                if not item:
                    self.slots[_hash].pop(index)
                    self.item_count -= 1
                else:
                    self.slots[_hash][index] = item

    def delete(self, key):
        _hash = self.hash(key)
        stored = self.search(key)
        if stored:
            self._update(_hash, key)

    def store(self, item):
        for key in item.keys():
            # 1. Check if object exists
            stored = self.search(key)
            _hash = self.hash(key)

            if stored:
                self._update(_hash, key, item)
            else:
                self._add(_hash, item)

        if self._should_re_hash():
            self._re_hash()

    def _re_hash(self):
        self.size = self.size * self.RE_HASH_SIZE_MULTIPLY
        self.item_count = 0 
        old_slots = self.slots
        self.slots = [[] for _ in range(self.size)]

        for slot in old_slots:
            for item in slot:
                key = list(item.keys())[0]
                _hash = self.hash(key)
                self.slots[_hash].append(item)
                self.item_count += 1

    def search(self, key: str):
        _hash = self.hash(key)
        slot = self.slots[_hash]
        for item in slot:
            if key in item:
                return item
        return None

    def _load_factor(self):
        if self.item_count == 0:
            return 0 
        return self.item_count / self.size

    def _should_re_hash(self):
        factor = self._load_factor()
        if factor > self.RE_HASH_FACTOR:
            return True
        else:
            return False

    def show(self):
        for i, slot in enumerate(self.slots):
            print(f"Slot {i}: {slot}")

table = HashTable(5)
person = {
    "yuri caetano": "CPF: 221.509.123-09"
}
person2 = {
    "yuari caetano": "CPF: 221.509.123-09"
}
table.store(person)
table.store(person2)
person = table.search('yuri caetano')
table.show()
print("=" * 10)


update_yuri= {
    "yuri caetano": "CPF: 222.222.222.-59"
}
table.store(update_yuri)
table.store({'yuri caetano2': '119841981299'})  # collision
table.show()


print("\n" + "=" * 10)
print("--- Testing DELETION ---")
print("HashTable BEFORE deleting 'yuri caetano2':")
table.show()

# Call to your new function!
table.delete('yuri caetano2')

print("\nHashTable AFTER deleting 'yuri caetano2':")
table.show()
ipdb.set_trace()