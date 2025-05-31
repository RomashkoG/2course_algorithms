n = int(input())
list = list(map(int, input().split()))

swap_count = 0
for i in range(n):
    for j in range(n - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
            swap_count += 1

print(swap_count)