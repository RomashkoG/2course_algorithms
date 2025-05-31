def f(x):
    return x**3 + x + 1

def solve():
    left = 0.0
    right = 10.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) > 5:
            right = mid
        else:
            left = mid

    print("%.7f" % right)

solve()

# answer = 1.3787968