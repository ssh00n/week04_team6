# 등차수열로 속도가 증가했을 때 k번째 돌에서 a만큼의 최대 속도를 가질 수 있고 이는 k = a(a + 1) / 2 를 만족한다.
# 정리하면 a = sqrt(2 * k + (1 / 4)) - 1 / 2 이기 때문에
# i번 위치에서 int(sqrt(2 * i)) + 1 까지 검사하면 가능한 모든 속도에서의 값을 조사할 수 있다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
small = set([int(input()) for _ in range(m)])

INF = int(1e9)
dp = [[INF] * int((2 * n) ** 0.5) + 2 for _ in range(n + 1)]
dp[1][0] = 1 # dp[돌][진입속도] = 점프 횟수

for i in range(2, n + 1): # 돌
    if i in small:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1): # 진입속도
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + 1

answer = min(dp[n])
print(answer if answer != INF else -1)

