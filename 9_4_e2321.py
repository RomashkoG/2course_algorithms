def quicksort(lst, left, right):
    if left >= right:
        return

    pivot = lst[(left + right) // 2]
    i, j = left, right

    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    quicksort(lst, left, j)
    quicksort(lst, i, right)

n = int(input())
lst = list(map(int, input().split()))

quicksort(lst, 0, n - 1)

print(*lst)