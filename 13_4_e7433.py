A = int(input())
P = int(input())

stack = []

while A > 0:
    remainder = A % P
    stack.append(remainder)
    A //= P

result = []
while stack:
    digit = stack.pop()
    if digit <= 9:
        result.append(str(digit))
    else:
        result.append(f'[{digit}]')

print(''.join(result) if result else '0')