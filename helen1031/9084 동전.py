import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for cost in range(1, m + 1):
            if cost < coin:
                continue
            else:
                dp[cost] = dp[cost] + dp[cost - coin]

    print(dp[m])