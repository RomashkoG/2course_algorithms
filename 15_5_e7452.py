class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def PrintReverse(self):
        class StackNode:
            def __init__(self, val, below=None):
                self.val = val
                self.below = below

        top = None
        current = self.head
        while current:
            top = StackNode(current.data, top)
            current = current.next

        while top:
            print(top.val, end=' ')
            top = top.below
        print()

n = int(input())
values = list(map(int, input().split()))

lst = List()
for v in values:
    lst.addToTail(v)

lst.Print()
lst.PrintReverse()