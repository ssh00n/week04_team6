import sys
sys.stdin = open('6_input.txt' ,'r')
input = sys.stdin.readline

n = int(input())

# 구현 문제 같아 보이지만 피보나치수 응용 피보나치 수열과 비슷하다
dp = [0] * 1000001


for i in range(1, n+1):
    # 1인 경우 15746을 나눈 나머지 저장
    if i == 1:
        dp[i] = 1 % 15746
    # 2인 경우 15746을 나눈 나머지 저장
    elif i == 2:
        dp[i] = 2 % 15746
    # 나머지의 합도 저장해서 나눠주면 원하는 수를 얻을 수 있다.
    else:
        dp[i] = (dp[i-1]  + dp[i-2]) % 15746

print(dp[n])