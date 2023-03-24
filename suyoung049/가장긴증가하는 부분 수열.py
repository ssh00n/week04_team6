import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = list(map(int, input().split()))

# 증가하는 부분 수열 의 수를 저장하기 위한 dp 배열 저장
dp = [1] * n

# 현재의 수까지 증가하는 수 저장
for i in range(1, n):
    # 앞의 수의 배열에서 i 보다 작은수가 있다면 dp에 max값 저장
    for j in range(i):
        if num_li[j] < num_li[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열에서 가장 큰수가 가장 긴 증가하는 부분 수열의 수
print(max(dp))
