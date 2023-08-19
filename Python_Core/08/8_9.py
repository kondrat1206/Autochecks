from collections import deque

MAX_LEN = 5

lifo = deque([], MAX_LEN)


def push(element):
    lifo.appendleft(element)
    print(list(lifo))
    return list(lifo)
    


def pop():
    result = lifo.popleft()
    print(result)
    return result