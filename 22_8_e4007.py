start = input().strip()
end = input().strip()

def neighbors(s):
    res = []
    if s[0] != '9':
        res.append(chr(ord(s[0]) + 1) + s[1:])
    if s[3] != '1':
        res.append(s[:3] + chr(ord(s[3]) - 1))
    res.append(s[1:] + s[0])
    res.append(s[-1] + s[:3])
    return res

queue = [start]
prev = {start: None}
i = 0

while i < len(queue):
    cur = queue[i]
    i += 1
    if cur == end:
        break
    for nxt in neighbors(cur):
        if nxt not in prev:
            prev[nxt] = cur
            queue.append(nxt)

path = []
node = end

while node is not None:
    path.append(node)
    node = prev[node]
path.reverse()

for x in path:
    print(x)