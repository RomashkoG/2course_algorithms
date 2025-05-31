class binary_heap():
    heap = []
    def __init__(self):
        self.heap = binary_heap.heap

    def add(self, id, priority):
        self.heap.append((id, priority))
        self.repair_up(len(self.heap) - 1)

    def change(self, id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i][0] == id:
                old_priority = self.heap[i][1]
                self.heap[i] = (id, new_priority)

                if new_priority > old_priority:
                    self.repair_up(i)
                else:
                    self.repair_down(i)
                break  # ⛔ не шукаємо далі

    def pop(self):
        if not self.heap:
            return
        print(f"{self.heap[0][0]} {self.heap[0][1]}")
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.repair_down(0)

    def repair_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] > self.heap[parent][1]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def repair_down(self, i):
        size = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            if right < size and self.heap[right][1] > self.heap[largest][1]:
                largest = right
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break


for i in range(30000):
    try:
        data = input().split()
    except EOFError:
        break
    if not data:
        continue
    if data[0] == "ADD":
        binary_heap().add(data[1], int(data[2]))
    elif data[0] == "POP":
        binary_heap().pop()
    elif data[0] == "CHANGE":
        binary_heap().change(data[1], int(data[2]))
