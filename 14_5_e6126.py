class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Queue:
    def __init__(self):
        self.head = None

    def push(self, value):
        def _push(node, v):
            if node is None:
                return Node(v)
            node.next = _push(node.next, v)
            return node
        self.head = _push(self.head, value)

    def pop(self):
        if self.head is None:
            return None
        v = self.head.value
        self.head = self.head.next
        return v

    def front(self):
        return None if self.head is None else self.head.value

    def size(self):
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.next)
        return _size(self.head)

    def clear(self):
        self.head = None

q = Queue()

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]

    if cmd == "push":
        n = int(parts[1])
        q.push(n)
        print("ok")
    elif cmd == "pop":
        v = q.pop()
        print(v if v is not None else "error")
    elif cmd == "front":
        v = q.front()
        print(v if v is not None else "error")
    elif cmd == "size":
        print(q.size())
    elif cmd == "clear":
        q.clear()
        print("ok")
    elif cmd == "exit":
        print("bye")
        break