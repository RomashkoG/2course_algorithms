def dfs(covered_mask, count):
    global best_count, best_solution
    if count >= best_count:
        return
    if covered_mask == ALL_MASK:
        best_count = count
        best_solution = cur_solution.copy()
        return
    uncovered_mask = (~covered_mask) & ALL_MASK
    uncovered_count = uncovered_mask.bit_count()
    lb = (uncovered_count + max_cover_size - 1) // max_cover_size
    if count + lb >= best_count:
        return
    lowbit = uncovered_mask & -uncovered_mask
    v = lowbit.bit_length() - 1
    for u in coverers[v]:
        new_covered = covered_mask | neighbor_mask[u]
        cur_solution.append(u)
        dfs(new_covered, count + 1)
        cur_solution.pop()
        if count + 1 >= best_count:
            break

N_R = input().split()
N = int(N_R[0])
R = int(N_R[1])
coords = []
for _ in range(N):
    x_y = input().split()
    x = int(x_y[0])
    y = int(x_y[1])
    coords.append((x, y))

R2 = R * R
neighbor_mask = [0] * N
for i in range(N):
    xi, yi = coords[i]
    mask = 0
    for j in range(N):
        xj, yj = coords[j]
        dx = xi - xj
        dy = yi - yj
        if dx*dx + dy*dy <= R2:
            mask |= (1 << j)
    neighbor_mask[i] = mask

ALL_MASK = (1 << N) - 1
coverers = [[] for _ in range(N)]
for u in range(N):
    mask_u = neighbor_mask[u]
    m = mask_u
    while m:
        lowbit = m & -m
        v = lowbit.bit_length() - 1
        coverers[v].append(u)
        m ^= lowbit

deg = [neighbor_mask[u].bit_count() for u in range(N)]
for v in range(N):
    coverers[v].sort(key=lambda u: -deg[u])

max_cover_size = max(deg)
best_count = N + 1
best_solution = []
cur_solution = []

dfs(0, 0)

best_solution_sorted = sorted(best_solution)
print(best_count)
print(" ".join(str(u+1) for u in best_solution_sorted))