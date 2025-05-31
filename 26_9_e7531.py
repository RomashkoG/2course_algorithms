n, m, p = map(int, input().split())
danger = [False] * n
if p > 0:
    for x in map(int, input().split()):
        danger[x - 1] = True

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if danger[u] and danger[v]:
        continue
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))
rank = [0] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

used = [False] * n
total = 0
count = 0

for w, u, v in edges:
    if danger[u] and used[u]:
        continue
    if danger[v] and used[v]:
        continue
    if union(u, v):
        total += w
        count += 1
        if danger[u]:
            used[u] = True
        if danger[v]:
            used[v] = True
        if count == n - 1:
            break

roots = set(find(i) for i in range(n))
if count == n - 1 and len(roots) == 1:
    print(total)
else:
    print("impossible")