class Stack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256):
        self._stk = [None] * capacity
        self._capacity = capacity
        self._ptr = 0

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._capacity

    def is_empty(self) -> bool:
        return self._ptr <= 0

    def is_full(self) -> bool:
        return self._ptr >= self._capacity

    def push(self, value: any) -> None:
        if self.is_full():
            raise Full()
        self._stk[self._ptr] = value
        self._ptr += 1

    def pop(self) -> any:
        if self.is_empty():
            raise Empty()

        self._ptr -= 1
        return self._stk[self._ptr]

