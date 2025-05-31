class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, v):
        node = Node(v)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def push_back(self, v):
        node = Node(v)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_front(self):
        if self.head is None:
            return None
        val = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return val

    def pop_back(self):
        if self.tail is None:
            return None
        val = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return val

    def front(self):
        return None if self.head is None else self.head.value

    def back(self):
        return None if self.tail is None else self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

dq = Deque()

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]

    if cmd == "push_front":
        n = int(parts[1])
        dq.push_front(n)
        print("ok")
    elif cmd == "push_back":
        n = int(parts[1])
        dq.push_back(n)
        print("ok")
    elif cmd == "pop_front":
        v = dq.pop_front()
        if v is None:
            print("error")
        else:
            print(v)
    elif cmd == "pop_back":
        v = dq.pop_back()
        if v is None:
            print("error")
        else:
            print(v)
    elif cmd == "front":
        v = dq.front()
        if v is None:
            print("error")
        else:
            print(v)
    elif cmd == "back":
        v = dq.back()
        if v is None:
            print("error")
        else:
            print(v)
    elif cmd == "size":
        print(dq.size())
    elif cmd == "clear":
        dq.clear()
        print("ok")
    elif cmd == "exit":
        print("bye")
        break