def is_heap(n, list):
    for i in range(n // 2):
        if 2 * i + 1 < n and list[i] > list[2 * i + 1]:
            return "NO"
        if 2 * i + 2 < n and list[i] > list[2 * i + 2]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    n = int(input())
    list = list(map(int, input().split()))
    print(is_heap(n, list))