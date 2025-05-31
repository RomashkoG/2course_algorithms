def function(arr, t):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, count_cross = merge_and_count(left, right)

        return merged, inv_left + inv_right + count_cross

    def merge_and_count(left, right):
        count = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > right[j] + t:
                j += 1
            count += j

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += left[i:]
        merged += right[j:]

        return merged, count

    _, total_count = merge_sort(arr)
    return total_count

n, t = map(int, input().split())
arr = list(map(int, input().split()))
print(function(arr, t))