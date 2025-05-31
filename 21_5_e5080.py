n = int(input())
deg = [0] * n
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            deg[i] += 1
count = 0
for i in deg:
    if i == 1:
        count += 1
print(count)