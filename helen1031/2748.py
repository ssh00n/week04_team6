n = int(input())
dp = [-1] * 91
dp[0] = 0
dp[1] = 1


def fibo(num):
    if dp[num] == -1:
        dp[num] = fibo(num - 1) + fibo(num - 2)

    return dp[num]


fibo(n)
print(dp[n])