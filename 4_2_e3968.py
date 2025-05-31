def f(x):
    return x * x + x ** 0.5

def solve(C):
    left = 0.0
    right = C
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) < C:
            left = mid
        else:
            right = mid

    print("%.7f" % left)

C = float(input())
solve(C)