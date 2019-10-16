"""
146. LRU Cache
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.used = []
    def get(self, key: int) -> int:

        if key in self.d:
            if self.used[0] != key:
                self.used.remove(key)
                self.used.insert(0, key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.d:
            self.d[key] = value
            if self.used[0] != key:
                self.used.remove(key)
                self.used.insert(0, key)

        if len(self.d) + 1 > self.capacity:
            rm_key = self.used.pop(-1)
            self.d.pop(rm_key)

        if key not in self.d:
            self.d[key] = value
            self.used.insert(0,key)

"""
OrderedDict keeps track of order of insertion for us using a linked list of the keys.
"""
from collections import OrderedDict

class LRUCache_:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyVals = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.keyVals:
            result = self.keyVals[key]
            del self.keyVals[key]
            self.keyVals[key] = result
            return result
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyVals:
            del self.keyVals[key]
        elif self.capacity == len(self.keyVals):
            del self.keyVals[next(iter(self.keyVals))]
        self.keyVals[key] = value

"""
双向链表
"""