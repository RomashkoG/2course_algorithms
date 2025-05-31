class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        first = self.head
        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2

    def Print(self) -> None:
        curr = self.head
        out = []
        while curr:
            out.append(str(curr.data))
            curr = curr.next
        print(" ".join(out))


try:
    n = int(input().strip())
except:
    n = 0
if n <= 0:
    exit()

values = list(map(int, input().strip().split()))
lst = List()
for v in values:
    lst.addToTail(v)

lst.ReorderList()
lst.Print()