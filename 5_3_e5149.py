def can_place(stalls, cows, distance):
    last = stalls[0]
    count = 1
    for x in stalls:
        if x - last >= distance:
            count += 1
            last = x
    return count >= cows

n, k = map(int, input().split())
stalls = list(map(int, input().split()))
stalls.sort()

left = 1
right = stalls[-1] - stalls[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_place(stalls, k, mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)