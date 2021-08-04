from enum import Enum
from collections import namedtuple
from fixed_queue import FixedQueue

Menus = namedtuple("Menu", "enqueue dequeue")

test = Menus(1, 2)
Menu = Enum("Menu", ["Enqueue", "Dequeue", "Peek", "Find", "Dump", "End"])

print(test.enqueue)


def select_menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep="    ", end="")
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)
print(q.find(1))

while True:
    print(f"data count : {len(q) % q.capacity}")
    menu = select_menu()

    if menu == Menu.Enqueue:
        x = int(input("input your data for enqueue : "))
        try:
            q.enqueue(x)
        except FixedQueue.Full:
            print("full")

    elif menu == Menu.Dequeue:
        try:
            x = q.dequeue()
            print(x)
        except FixedQueue.Empty:
            print("empty")

    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(x)

        except FixedQueue.Empty:
            print("empty")

    elif menu == Menu.End:
        break
