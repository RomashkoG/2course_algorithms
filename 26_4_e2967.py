import math

n = int(input())
coords = [tuple(map(float, input().split())) for _ in range(n)]

INF = float('inf')
dist_sq = [INF] * n
visited = [False] * n

dist_sq[0] = 0.0
total = 0.0

for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not visited[i] and dist_sq[i] < best:
            best = dist_sq[i]
            u = i
    visited[u] = True
    total += math.sqrt(best)
    ux, uy = coords[u]
    for v in range(n):
        if not visited[v]:
            vx, vy = coords[v]
            dx = ux - vx
            dy = uy - vy
            d2 = dx*dx + dy*dy
            if d2 < dist_sq[v]:
                dist_sq[v] = d2

print(f"{total:.3f}")