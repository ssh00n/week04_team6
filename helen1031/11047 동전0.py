import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

cnt = 0
for coin in coins:
    if coin > k:
        continue
    else:
        cnt += k // coin
        k = k - k // coin * coin

print(cnt)