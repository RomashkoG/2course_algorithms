n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
in_deg = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    in_deg[v] += 1

queue = []
for i in range(1, n + 1):
    if in_deg[i] == 0:
        queue.append(i)

res = []
while queue:
    u = queue.pop(0)
    res.append(u)
    for v in g[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)

if len(res) == n:
    print(' '.join(map(str, res)))
else:
    print(-1)