def f(x):
    return x**3 + 4*x**2 + x - 6

def solve():
    left = 0.0
    right = 2.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) * f(left) <= 0:
            right = mid
        else:
            left = mid

    print("%.7f" % left)

solve()

# answer = 0.9999999