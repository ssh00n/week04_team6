import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

w = [list(map(int, input().split())) for _ in range(n)]
size = 2 ** (n-1)
INF = sys.maxsize
dp = [[INF] * size for _ in range(n)]


def get_minium(n, w, j, route, dp):
    mini_dist = INF
    for i in range(1, n):
        if isin(i, route):
            before_route = diff(route, i)
            dist = w[j][i] + dp[i][before_route]
            if mini_dist > dist:
                mini_dist = dist
    
    return mini_dist

def diff(route, j):
    t = 1 << (j-1)
    return (route & (~t))


def isin(j, route):
    if route & (1 << j-1) != 0:
        return True
    else:
        return False

def counting(route, n):
    count_ = 0
    for i in range(1, n):
        if route & (1 << i - 1) != 0:
            count_ += 1
    
    return count_

def solution(n, w, dp):
    for j in range(n):
        for i in range(n):
            if not w[j][i]:
                w[j][i] = INF


    for i in range(1, n):
        dp[i][0] = w[i][0]
    
    for k in range(1, n-1):
        for route in range(1, size):
            if counting(route, n) == k:
                for j in range(1, n): 
                    if not isin(j, route):
                        dp[j][route] = get_minium(n, w, j, route, dp)


    dp[0][size-1] = get_minium(n, w, 0, size-1, dp)

    return dp[0][size -1]

print(solution(n, w, dp))
