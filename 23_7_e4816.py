n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
components = []

for i in range(1, n + 1):
    if not visited[i]:
        stack = [i]
        visited[i] = True
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        components.append(comp)

print(len(components))
for comp in components:
    print(len(comp), *comp)