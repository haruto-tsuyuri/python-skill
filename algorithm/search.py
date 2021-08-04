"""

use sentinel
"""
from abc import ABC
from array import array
from copy import deepcopy

from typing import Any
import hashlib


def seq_search(ay: array, key: Any) -> int or False:
    a = deepcopy(ay)
    a.append(key)

    for index, value in enumerate(a, start=0):
        print(f"{value},{index}")
        if value == key:
            return index

    return False


ary = array("H", [1, 2, 3, 4, 5, 6])
index_number = seq_search(ary, 3)


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity


class Node:
    key = None

    def __init__(self, key: Any, value: Any, nxt) -> None:
        self.key = key
        self.val = value
        self.nxt = nxt


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Node] * self.capacity

    def __hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash_value = self.__hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            if p.key == key:
                return p.value
