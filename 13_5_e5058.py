s = input().strip()
stack = []

pairs = {')': '(', ']': '[', '}': '{'}

valid = True
for char in s:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack or stack[-1] != pairs[char]:
            valid = False
            break
        stack.pop()

if valid and not stack:
    print("yes")
else:
    print("no")