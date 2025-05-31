n = int(input())

temp = n
bits = 0
while temp > 0:
    bits += 1
    temp //= 2

max_val = n
current = n

for i in range(1, bits):
    left_shift = (current << 1)
    carry = (current >> (bits - 1))
    current = left_shift | carry
    current = current & ((1 << bits) - 1)

    if current > max_val:
        max_val = current

print(max_val)