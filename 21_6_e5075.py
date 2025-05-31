n, m = map(int, input().split())
in_deg = [0] * (n + 1)
out_deg = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    out_deg[u] += 1
    in_deg[v] += 1

for i in range(1, n + 1):
    print(in_deg[i], out_deg[i])