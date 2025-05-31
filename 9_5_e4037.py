def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

n = int(input())
robots = [tuple(map(int, input().split())) for _ in range(n)]

sorted_robots = merge_sort(robots)

for r in sorted_robots:
    print(r[0], r[1])