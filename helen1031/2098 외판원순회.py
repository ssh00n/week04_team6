import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 비트마스킹으로 방문처리하여 메모리초과 방지
ALL_VISIT = (1 << n) - 1

dp = [[None] * (1 << n) for _ in range(n)]
INF = int(1e9)

def dfs(last, visited):
    # 모든 도시를 방문했다면
    if visited == ALL_VISIT:
        # last도시 -> 0번 도시 루트가 존재하면 리턴, 없으면 INF
        return graph[last][0] or INF

    # 이미 계산한 dp 값이 있다면 dp 테이블에서 값 찾아서 리턴
    if dp[last][visited] is not None:
        return dp[last][visited]

    tmp = INF
    for city in range(n):
        # 해당 도시를 아직 방문하지 않았고, 이전도시 -> city로의 루트가 존재한다면
        if visited & (1 << city) == 0 and graph[last][city] != 0:
            tmp = min(tmp, dfs(city, visited | (1 << city)) + graph[last][city])
    dp[last][visited] = tmp

    return dp[last][visited]

print(dfs(0, 1 << 0))