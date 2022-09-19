class HashTable(object):
    def __init__(self, size):
        self.data = [None for _ in range(size)]

    def _hash(self, key):
        generated_hash = 0
        for i in range(0, len(key)):
            generated_hash = (generated_hash + ord(key[i]) * i) % len(self.data)
        return generated_hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        print(current_bucket)

        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        keys_array = []
        for keys in self.data:
            keys_array.append(keys[0][0])
        return keys_array


my_hash_table = HashTable(2)
my_hash_table.set('grapes', 10000)
my_hash_table.set('apple', 13400)
my_hash_table.set('apples', 15400)
# print(my_hash_table.get('apples'))
# print(my_hash_table.data)
print(my_hash_table.keys())
