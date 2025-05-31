n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

k = int(input())
starts = list(map(int, input().split()))

dist = [-1] * (n + 1)
current_stack = []
for s in starts:
    if dist[s] == -1:
        dist[s] = 0
        current_stack.append(s)

max_time = 0
next_stack = []

while current_stack:
    node = current_stack.pop()
    for nei in adj[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            if dist[nei] > max_time:
                max_time = dist[nei]
            next_stack.append(nei)
    if not current_stack:
        current_stack, next_stack = next_stack, []

last_vertex = 1
for i in range(1, n + 1):
    if dist[i] == max_time:
        last_vertex = i
        break

print(max_time)
print(last_vertex)