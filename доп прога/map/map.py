class Map:
    def __init__(self, capacity, collision_resolution_method="chaining"):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.collision_resolution_method = collision_resolution_method

        if self.collision_resolution_method == "chaining":
            self.collision_resolution = self._chained_resolution
        elif self.collision_resolution_method == "open_addressing":
            self.collision_resolution = self._open_addressing
        else:
            raise ValueError(f"Invalid collision resolution method: {self.collision_resolution_method}")

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash(key) % self.capacity
        if self.table[index] is not None:
            for k, _ in self.table[index]:
                if k == key:
                    return True
        return False

    def insert(self, key, value):
        index = self._hash(key) % self.capacity

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.collision_resolution(index, key, value)

        self.size += 1

    def get(self, key):
        index = self._hash(key) % self.capacity

        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v

        return None

    def delete(self, key):
        index = self._hash(key) % self.capacity

        if self.table[index] is not None:
            original_size = len(self.table[index])
            self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
            if len(self.table[index]) < original_size:
                self.size -= 1

    def _hash(self, key):
        return hash(key)

    def _chained_resolution(self, index, key, value):
        self.table[index].append((key, value))

    def _open_addressing(self, index, key, value):
        i = 0
        while True:
            new_index = (index + i) % self.capacity
            if self.table[new_index] is None:
                self.table[new_index] = (key, value)
                break
            i += 1

# Example usage
my_map = Map(10, collision_resolution_method="chaining")
my_map.insert("apple", 1)
my_map.insert("banana", 2)
my_map.insert("cherry", 3)

print(my_map.get("banana"))  # Output: 2
print(len(my_map))  # Output: 3
print("apple" in my_map)  # Output: True

my_map.delete("banana")
print(len(my_map))  # Output: 2

# Using open addressing
my_map_open_addressing = Map(10, collision_resolution_method="open_addressing")
my_map_open_addressing.insert("apple", 1)
my_map_open_addressing.insert("banana", 2)
my_map_open_addressing.insert("cherry", 3)

print(my_map_open_addressing.get("banana"))  # Output: 2
print(len(my_map_open_addressing))  # Output: 3
print("apple" in my_map_open_addressing)  # Output: True

my_map_open_addressing.delete("banana")
print(len(my_map_open_addressing))  # Output: 2