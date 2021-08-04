class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        print("Is full")

    class NotFound(Exception):
        print("Not Founded")

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.no = 0
        self.front = 0
        self.rear = 0
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enqueue(self, x: any) -> None:
        if self.is_full():
            raise Full()
        self.que[self.rear] = x
        self.no += 1
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> any:
        if self.is_empty():
            raise FixedQueue.Empty()
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> any:
        if self.is_empty():
            raise FixedQueue.Empty()
        return self.que[self.front]

    def find(self, value: any) -> any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return FixedQueue.NotFound()

    def count(self, value: any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value) -> bool:
        return self.find(value) == type(int)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print("que is empty.")
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end='')
