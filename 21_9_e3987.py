n, m = map(int, input().split())
connected = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    connected[u][v] = 1
    connected[v][u] = 1

is_complete = True
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if connected[i][j] == 0:
            is_complete = False

print("YES" if is_complete else "NO")