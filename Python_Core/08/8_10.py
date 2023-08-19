from collections import deque

MAX_LEN = 5

fifo = deque([], MAX_LEN)


def push(element):
    fifo.append(element)
    print(list(fifo))
    return list(fifo)
    


def pop():
    result = fifo.popleft()
    print(result)
    return result