while True:
    try:
        n = int(input())
        if n == 0:
            break
        while True:
            line = input()
            if line == "0":
                print()
                break

            desired = list(map(int, line.split()))
            stack = []
            current = 1
            possible = True

            for target in desired:
                while current <= n and (not stack or stack[-1] != target):
                    stack.append(current)
                    current += 1
                if stack[-1] == target:
                    stack.pop()
                else:
                    possible = False
                    break

            print("Yes" if possible else "No")

    except EOFError:
        break
