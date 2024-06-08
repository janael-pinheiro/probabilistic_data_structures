from numpy import zeros
from mmh3 import hash


class CountMinSketch:
    def __init__(self, number_counters: int, number_hash_functions: int):
        self.__number_counters = number_counters
        self.__number_hash_functions = number_hash_functions
        self.__sketch = zeros((number_hash_functions, number_counters))

    def update(self, item, count: int = 1):
        for i in range(self.__number_hash_functions):
            index = hash(item, i) % self.__number_counters
            self.__sketch[i][index] += count

    def estimate(self, item) -> int:
        frequencies = []
        for i in range(self.__number_hash_functions):
            index = hash(item, i) % self.__number_counters
            frequencies.append(self.__sketch[i][index])
        return min(frequencies)

    def __setitem__(self, key, value):
        self.update(key, value)

    def __getitem__(self, item):
        return self.estimate(item)
