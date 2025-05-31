def solve(N, t, tracks):
    best_sum = [0]

    def backtrack(idx, current_sum):
        if current_sum > best_sum[0]:
            best_sum[0] = current_sum
        if best_sum[0] == N or idx == t:
            return
        
        for j in range(idx, t):
            next_sum = current_sum + tracks[j]
            if next_sum <= N:
                backtrack(j + 1, next_sum)

    backtrack(0, 0)
    return best_sum[0]

try:
    while True:
        line = input().strip()
        if not line:
            continue
        parts = line.split()
        N = int(parts[0])
        t = int(parts[1])

        tracks = list(map(int, parts[2:]))

        while len(tracks) < t:
            extra = input().split()
            for x in extra:
                if len(tracks) < t:
                    tracks.append(int(x))
                else:
                    break

        best = solve(N, t, tracks)
        print(f"sum:{best}")
except EOFError:
    pass