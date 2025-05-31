t = int(input())
for _ in range(t):
    line = input()
    while line.strip() == '':
        line = input()
    R, C = map(int, line.split())
    grid = []
    for _ in range(R):
        row = input()
        if len(row) < C:
            row = row + ' ' * (C - len(row))
        grid.append(list(row))

    sr = sc = lr = lc = tr = tc = -1, -1, -1, -1, -1, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'g':
                sr, sc = i, j
            elif grid[i][j] == 'l':
                lr, lc = i, j
            elif grid[i][j] == 'e':
                tr, tc = i, j

    INF = 10**9
    distL = [[INF] * C for _ in range(R)]
    q = [(lr, lc)]
    distL[lr][lc] = 0
    head = 0
    while head < len(q):
        r, c = q[head]
        head += 1
        d0 = distL[r][c] + 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] != 'R' and grid[rr][cc] != 'e' and distL[rr][cc] > d0:
                    distL[rr][cc] = d0
                    q.append((rr, cc))

    found = False
    distG = [[INF] * C for _ in range(R)]
    if distL[sr][sc] > 0:
        distG[sr][sc] = 0
        q = [(sr, sc)]
    else:
        q = []
    head = 0
    while head < len(q):
        r, c = q[head]
        head += 1
        t0 = distG[r][c]
        if t0 > 1000:
            continue
        if r == tr and c == tc:
            found = True
            break
        t1 = t0 + 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] != 'R' and t1 < distL[rr][cc] and t1 < distG[rr][cc]:
                    distG[rr][cc] = t1
                    q.append((rr, cc))

    if not found and distG[tr][tc] <= 1000:
        found = True

    print("YES" if found else "NO")