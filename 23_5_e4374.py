n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

k = int(input())
queries = []
for _ in range(k):
    parts = list(map(int, input().split()))
    c = parts[0]
    removed = set(parts[1:])
    queries.append(removed)

def dfs(v, visited, g):
    visited[v] = True
    for u in g[v]:
        if not visited[u]:
            dfs(u, visited, g)

for removed in queries:
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        if (i + 1) not in removed:
            u, v = edges[i]
            g[u].append(v)
            g[v].append(u)
    visited = [False] * (n + 1)
    dfs(1, visited, g)
    connected = True
    for i in range(1, n + 1):
        if not visited[i]:
            connected = False
            break
    print("Connected" if connected else "Disconnected")