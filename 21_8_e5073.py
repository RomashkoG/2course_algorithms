n, m = map(int, input().split())
edges = set()
has_multi = False

for _ in range(m):
    u, v = map(int, input().split())
    if (u, v) in edges:
        has_multi = True
    edges.add((u, v))

print("YES" if has_multi else "NO")