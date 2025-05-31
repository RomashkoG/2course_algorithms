m, n = map(int, input().split())
g = [list(input().strip()) for _ in range(m)]

vis = [[False] * n for _ in range(m)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

for i in range(m):
    for j in range(n):
        if g[i][j] == '#' and not vis[i][j]:
            ans += 1
            stack = [(i, j)]
            vis[i][j] = True

            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < m and 0 <= cc < n:
                        if g[rr][cc] == '#' and not vis[rr][cc]:
                            vis[rr][cc] = True
                            stack.append((rr, cc))

print(ans)