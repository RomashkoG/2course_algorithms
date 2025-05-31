import math

def f(x):
    return math.sin(x) - x / 3

def solve():
    left = 1.6
    right = 3.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) * f(left) <= 0:
            right = mid
        else:
            left = mid

    print("%.7f" % left)

solve()

# answer = 2.2788626