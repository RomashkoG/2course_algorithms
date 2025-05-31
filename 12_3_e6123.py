class Stack:
    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self):
        if not self._data:
            return None
        return self._data.pop()

    def back(self):
        if not self._data:
            return None
        return self._data[-1]

    def size(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()


stack = Stack()

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
        stack.push(n)
        print("ok")

    elif cmd == "pop":
        val = stack.pop()
        if val is None:
            print("error")
        else:
            print(val)

    elif cmd == "back":
        val = stack.back()
        if val is None:
            print("error")
        else:
            print(val)

    elif cmd == "size":
        print(stack.size())

    elif cmd == "clear":
        stack.clear()
        print("ok")

    elif cmd == "exit":
        print("bye")
        break

    else:
        continue