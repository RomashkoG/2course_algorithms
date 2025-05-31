def lower_bound(list, x):
    left = 0
    right = len(list)
    while left < right:
        mid = (left + right) // 2
        if list[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, x):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
if n > 0:
    animals = list(map(int, input().split()))
else:
    animals = []

m = int(input())
queries = list(map(int, input().split()))

for i in queries:
    print(upper_bound(animals, i) - lower_bound(animals, i))