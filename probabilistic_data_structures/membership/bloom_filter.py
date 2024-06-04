import math

import mmh3
from numpy import zeros


class BloomFilter:
    def __init__(self, capacity: int, error_rate: float):
        self.__capacity = capacity
        self.__error_rate = error_rate
        self.__number_bits = self.__get_number_bits()
        self.__number_hash_functions = self.__get_number_hash_functions()
        self.__bit_array = zeros(self.__number_bits)

    def __contains__(self, item):
        return self.may_contains(item)

    def add(self, element: str) -> None:
        for i in range(self.__number_hash_functions):
            hash_value = mmh3.hash(element, i) % self.__number_bits
            self.__bit_array[hash_value] = 1

    def may_contains(self, element) -> bool:
        for i in range(self.__number_hash_functions):
            hash_value = mmh3.hash(element, i) % self.__number_bits
            if self.__bit_array[hash_value] == 0:
                return False
        return True

    def __get_number_bits(self) -> int:
        num_bits = - (self.__capacity * math.log(self.__error_rate)) / (math.log(2) ** 2)
        return int(num_bits)

    def __get_number_hash_functions(self) -> int:
        num_hashes = (self.__number_bits / self.__capacity) * math.log(2)
        return int(num_hashes)
