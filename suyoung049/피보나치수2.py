import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

# 입력값 받기
n = int(input())

# 주어진 input 값의 범위가 90까지
dp = [0] * 91


#점화식 구현
for i in range(n+1):
    # 0번째 피보나치
    if i == 0:
        dp[i] = 0
    # 1번째 피보나치
    elif i == 1:
        dp[i] = 1
    # 점화식 a[i] = a[i-1] + a[i-2]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])