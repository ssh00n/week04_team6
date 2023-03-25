import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

# 점화식을 만드는게 중요
# 1원과 2원 짜리 동전으로 7원을 만든는 방법은 

# 2+2+2+1 = 7
# 2+2+1+1+1 = 7
# 2+1+1+1+1+1 = 7

# 즉 7-2 인 5원을 1원과 2원짜리로 만드는 경우의 수와 같음


for _ in range(T):

    n = int(input())


    num_li = [0] + list(map(int, input().split()))

    k = int(input())

    # 각 숫자 마다 만들어 질수 있는 수의 경우의 수를 합치기 편하게 하기 위해 주어진 동전을 열 만들 수를 행으로 만듬
    dp = [[0] * (n+1) for _ in range(k+1)] 

    for i in range(1, n+1):
        for j in range(1, k+1):
            
            # 만들어야 할 수가 동전의 크기와 같다면 경우의 수 1로 변경
            if j == num_li[i]:
                dp[j][i] = 1
            
            # 만들어야 할수가 주어진 동전의 크기보다 크다면 만들어야 할 값 에 동전의 크기를 뺀 수를 만든 모든 경우의 수
            elif num_li[i] < j:
                dp[j][i] = sum(dp[j-num_li[i]])

    print(sum(dp[k]))
                



