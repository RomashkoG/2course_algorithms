def karatsuba(x, y):
    x = str(x)
    y = str(y)

    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)

    n = max(len(x), len(y))
    half = n // 2

    x = x.zfill(n)
    y = y.zfill(n)

    x_high = int(x[:-half])
    x_low = int(x[-half:])
    y_high = int(y[:-half])
    y_low = int(y[-half:])

    z0 = karatsuba(x_low, y_low)
    z2 = karatsuba(x_high, y_high)
    z1 = karatsuba(x_low + x_high, y_low + y_high) - z0 - z2

    return z2 * 10**(2 * half) + z1 * 10**half + z0


A, B = input().split()

print(karatsuba(A, B))