try:
    while True:
        n = int(input())
        heights = list(map(int, input().split()))
        a, b = map(int, input().split())

        count = 0
        for h in heights:
            if a <= h <= b:
                count += 1

        print(count)
except EOFError:
    pass