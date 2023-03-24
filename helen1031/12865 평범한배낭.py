import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i, item in enumerate(items):
    weight, value = item
    for j in range(1, k + 1):
        if weight > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(dp[-1][-1])