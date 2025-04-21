class binary_heap:
    def __init__(self):
        self.heap = []
        self.index_map = {}

    def add(self, id, priority):
        self.heap.append((id, priority))
        self.index_map[id] = len(self.heap) - 1
        self.sift_up(len(self.heap) - 1)

    def change(self, id, priority):
        index = self.index_map[id]
        old_priority = self.heap[index][1]
        self.heap[index] = (id, priority)
        if priority > old_priority:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def pop(self):
        if not self.heap:
            return
        top_id, top_priority = self.heap[0]
        print(f"{top_id} {top_priority}")
        last = self.heap.pop()
        del self.index_map[top_id]
        if self.heap:
            self.heap[0] = last
            self.index_map[last[0]] = 0
            self.sift_down(0)

    def sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][1] > self.heap[parent][1]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                self.index_map[self.heap[idx][0]] = idx
                self.index_map[self.heap[parent][0]] = parent
                idx = parent
            else:
                break

    def sift_down(self, idx):
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < size and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            if right < size and self.heap[right][1] > self.heap[largest][1]:
                largest = right
            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                self.index_map[self.heap[idx][0]] = idx
                self.index_map[self.heap[largest][0]] = largest
                idx = largest
            else:
                break


heap = binary_heap()

for i in range(30000):
    try:
        data = input().split()
    except EOFError:
        break
    cmd = data[0]
    if cmd == "ADD":
        heap.add(data[1], int(data[2]))
    elif cmd == "POP":
        heap.pop()
    elif cmd == "CHANGE":
        heap.change(data[1], int(data[2]))