n, k, a, b, d = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(k):
    u, v = map(int, input().split())
    g[u].append(v)

stack = [(a, 0, set([a]))]
count = 0

while stack:
    node, depth, visited = stack.pop()
    if depth > d:
        continue
    if node == b:
        count += 1
        continue
    for neighbor in g[node]:
        if neighbor not in visited:
            stack.append((neighbor, depth + 1, visited | {neighbor}))

print(count)