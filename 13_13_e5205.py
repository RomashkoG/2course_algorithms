MOD = 301907
s = input().strip()
n = len(s)

dp = [[0] * n for i in range(n)]

for length in range(2, n + 1, 2):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i + 1, j + 1, 2):
            if (s[i] == '(' or s[i] == '?') and (s[k] == ')' or s[k] == '?'):
                left = dp[i + 1][k - 1] if k - i > 1 else 1
                right = dp[k + 1][j] if k < j else 1
                dp[i][j] = (dp[i][j] + left * right) % MOD

print(dp[0][n - 1])