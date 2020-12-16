class Row:

    def __init__(self):
        self.row = []

    def get(self, key):
        for (k, v) in self.row:
            if k == key:
                return v
        return -1

    def put(self, key, val):
        # check if we need to update first
        for i, kv in enumerate(self.row):
            # update if key already exists
            if kv[0] == key:
                self.row[i] = (key, val)
                return

        # add new/unique entry via chaining
        self.row.append((key, val))

    def remove(self, key):
        for i, kv in enumerate(self.row):
            if kv[0] == key:
                del self.row[i]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # for hashing with modulus to ensure idx 0-2016
        self.key_space = 2017
        # init array with size = key_space
        self.hash_map = [Row() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = key % self.key_space
        self.hash_map[hash_value].put(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = key % self.key_space
        return self.hash_map[hash_value].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = key % self.key_space
        self.hash_map[hash_value].remove(key)