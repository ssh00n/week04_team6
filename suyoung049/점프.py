import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# 필요 요소 
# 못 건너는 돌 위치를 저장 할 리스트
# 현재 돌 까지 점프해서 올 수 있는 이전 돌의 점프 횟수를 기록할 2차원 dp배열
# 그리고 j를 현재 위치, i를 현재 속도라고 가정
# dp[j][i] = min(dp[j-i][i-1], dp[j-i][i], dp[j-i][i+1]) + 1
# 이라는 점화식을 얻을 수가 있다.
# 이 점화식은 j라는 점에 i의 속도로 도달 했을 때의 최소 점프횟수는 j-i의 위치에 각각 i-1, i, i+1의 속도로 도달했을때
# 최소 점프횟수 +1 이라는 뜻이다.
# i-1, i, i+1 속도에서 각각 +1, +0, -1을 했을 때 i 만큼 점프 할 수 있기 때문에 j-i 에서 j로 갈 수 있다
# 그리고 이 때 i의 최대값은 int((2*j)**0.5) + 1이다.

n, m = map(int, input().split())

def pprint(list_):
    for row in list_:
        print(row)
# 점프 할 수 없는 작은 돌 리스트 셋으로 저장
block_stone = set()

# 입력으로 주어진 작은 돌 셋에 저장
for _ in range(m):
    small = int(input())
    block_stone.add(small)

INF = sys.maxsize
# 열의 최대값은 int((2*n)**0.5) + 1 이다.
# 첫째항이 1이고 공차가 1인 등차 수열에서 수열의 합이 N이 될 때 마지막 항의 값의 근사값이다.
dp = [[INF] * (int((2*n)**0.5)+2) for _ in range(n+1)]

# 첫 돌의 위치는 1과 점프 거리는 0으로 저장
dp[1][0] = 0

for j in range(2, n+1):
    if j in block_stone:
    # 돌이 만약 작은 돌 리스트에 있다면 continue
        continue
    
    # 점프 거리는 1부터  int((2*j)**0.5) + 1이다.
    # 등차 수열의 합이 j 일때 마지막 항의 근사값
    for i in range(1, int((2 * j) ** 0.5) + 1):
        # i-1, i, i+1 속도에서 각각 +1, +0, -1을 했을 때 i 만큼 점프 할 수 있기 때문에 j-i 에서 j로 갈 수 있다
        # 위의 세 점프 거리의 최소값에서 1을 더한 값이 현재 돌로 올 수 있는 점프 횟수
        dp[j][i] = min(dp[j-i][i-1], dp[j-i][i], dp[j-i][i+1]) + 1

pprint(dp)


# 만약 dp의 값이 INF 라면 갈 수 없는 돌 -1 출력
if min(dp[n]) == INF:
    print(-1)
else:
    # 아니라면 점프 횟수 출력
    print(min(dp[n]))