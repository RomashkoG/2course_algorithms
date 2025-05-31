def push(heap, node):
    heap.append(node)
    i = len(heap) - 1
    while i > 0:
        p = (i - 1) >> 1
        if heap[i][0] < heap[p][0]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break

def pop(heap):
    last = heap.pop()
    if not heap:
        return last
    root = heap[0]
    heap[0] = last
    n = len(heap)
    i = 0
    while True:
        l = (i << 1) + 1
        r = l + 1
        if l >= n:
            break
        m = l
        if r < n and heap[r][0] < heap[l][0]:
            m = r
        if heap[m][0] < heap[i][0]:
            heap[i], heap[m] = heap[m], heap[i]
            i = m
        else:
            break
    return root

N = int(input())
Na = int(input())
A = list(map(int, input().split()))
Nb = int(input())
B = list(map(int, input().split()))

a_min = min(A)
b_min = min(B)
low = 0
high = max(N * a_min, N * b_min)

def can(T):
    mA = [T // a for a in A]
    if sum(mA) < N:
        return False
    mB = [T // b for b in B]
    if sum(mB) < N:
        return False
    heapA = []
    for ai, cnt in zip(A, mA):
        if cnt > 0:
            push(heapA, (ai, ai, 1))
    A_small = [0] * N
    for i in range(N):
        t, ai, k = pop(heapA)
        A_small[i] = t
        nxt = k + 1
        if nxt <= T // ai:
            push(heapA, (nxt * ai, ai, nxt))
    heapB = []
    for bi, cnt in zip(B, mB):
        if cnt > 0:
            last = cnt * bi
            push(heapB, (-last, bi, cnt))
    B_large = [0] * N
    for i in range(N):
        neg, bi, k = pop(heapB)
        t = -neg
        B_large[N - 1 - i] = t
        prev = k - 1
        if prev >= 1:
            push(heapB, (-(prev * bi), bi, prev))
    for i in range(N):
        if A_small[i] > B_large[i]:
            return False
    return True

if not can(high):
    h = high
    while not can(h):
        h <<= 1
    low = high + 1
    high = h

while low < high:
    mid = (low + high) >> 1
    if can(mid):
        high = mid
    else:
        low = mid + 1

print(low)