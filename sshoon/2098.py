# TSP(Traveling Salesman problem)
import sys
# sys.setrecursionlimit(10**4)

input = sys.stdin.readline

n = int(input())
INF = 1000001
dp = [[INF]*(1<<n) for _ in range(n)]
def dfs(x, visited):
    
    if visited == (1 << n) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF
        
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    for i in range(1, n):
        if not graph[x][i]:
            continue
        if visited & (1 << i):
            continue
        
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    
    return dp[x][visited]


graph = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, 1))