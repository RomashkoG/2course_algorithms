n = int(input())
grid = [list(input().strip()) for _ in range(n)]

sr = sc = er = ec = -1
for i in range(n):
    for j in range(n):
        if grid[i][j] == '@':
            sr, sc = i, j
        elif grid[i][j] == 'X':
            er, ec = i, j

visited = [[False]*n for _ in range(n)]
parent = [[None]*n for _ in range(n)]
queue = [(sr, sc)]
head = 0
visited[sr][sc] = True

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

found = False
while head < len(queue):
    r, c = queue[head]
    head += 1
    if r == er and c == ec:
        found = True
        break
    for dr, dc in dirs:
        rr, cc = r+dr, c+dc
        if 0 <= rr < n and 0 <= cc < n:
            if not visited[rr][cc] and (grid[rr][cc] == '.' or grid[rr][cc] == 'X'):
                visited[rr][cc] = True
                parent[rr][cc] = (r, c)
                queue.append((rr, cc))

if not found:
    print('N')
else:
    r, c = er, ec
    while not (r == sr and c == sc):
        if grid[r][c] != 'X':
            grid[r][c] = '+'
        else:
            grid[r][c] = '+'
        r, c = parent[r][c]
        
    print('Y')
    for row in grid:
        print(''.join(row))