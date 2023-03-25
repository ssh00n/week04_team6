import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
for _ in range(n-1):
    a, b = map(int, input().split())
    nums.append(b)
# nums 배열에 숫자 중복되지 않도록 삽입

dp = [[0] * n for _ in range(n)]
for d in range(1, n): # 대각선
    for i in range(0, n - d): # 행
        j = i + d # 열
        dp[i][j] = 2 ** 31 # 최대값으로 갱신
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i] * nums[k+1] * nums[j+1])