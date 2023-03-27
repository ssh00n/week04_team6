import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

# 연쇄 행렬 곱셉
# 1단계: 재귀 관계식을 찾는다.
# - 목표: Ai....Aj 행렬을 (Ai...Ak)(Ak+1....Aj)로 분할하는 재귀 관계식 찾기

# 2단계: 상향식 방법으로 해답을 구한다.
# - 초기화: M[j][i] = 0
# - 최종 목표 : M[1][n]

# 분할 정복(Divide - and - Conquer)
# - n 개의 행렬은 두개의 최적 부분 행렬의 곱으로 분할
# - 각 분할의 곱셈 횟수:
# - 각 부분 행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
# - M[1][k] + M[k+1][6] + (d[i-1] * d[k] * d[j])
# 최적 분할 : min(M[1][k] + M[k+1][6] + (d[i-1] * d[k] * d[j]))

# 행렬 곱의 최적 분할을 보기위한 함수
def order(p, i, j):
    if i == j:
        print('A%d'%(i), end='')
        return
       
    else:
        k = p[i][j]
        print('(', end='')
        order(p, i, k)
        order(p, k+1, j)
        print(')', end='')
        return
       

n = int(input())

# 행렬의 행 과 열을 저장하기 위한 리스트
procession = []

for _ in range(n):
    # 행의 개수만큼 행과 열을 저장
    y, x = map(int, input().split())
    procession.append((y,x))

d = []
# 첫 행렬은 행과 열을 모두 저장 다음 행렬 부터는 열만 저장(전 행렬의 열이 행이기 때문에 저장 불필요)
for i in range(n):
    if i == 0:
        d.append(procession[i][0])
        d.append(procession[i][1])
    
    else:
        d.append(procession[i][1])

# 곱셈 연산의 최소값을 구하기 위한 dp 배열
dp = [[0] * (n +1) for _ in range(n+1)]
# 최적분할 하는 분기점 k를 저장하기 위한 배열
dp_re = [[0] * (n+1) for _ in range(n+1)]

INF = sys.maxsize
# 행렬의 곱은 연산의 순서를 바꿔도 연산의 최소값은 같기 때문에 2차원 배열의 대각선의 오른쪽 위만 구해도 최적분할을 알 수 있다.
for digonal in range(1, n):
    # 2차원 배열 대각선 오른쪽 위의 인덱스를 알기위한 range
    for j in range(1, n-digonal+1):
        answer = INF
        # 대각 선 오른쪽 위는 행의 인덱스가 열의 인덱스 보다 항상 작다.
        i = j+digonal
        # 행렬을 분기하는 K는 dp[1][3] 일 경우 1<= k < 3이다.
        # 위의 행렬의 연산의 분기는 1. (Al * A2) * A3 , 2. Al * (A2 * A3) 이다.
        k = j

        while True:
            # 위의 분기별로 분할한 각 부분 행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수은 k 값에 따른 최소값 갱신
            # dp[1][3]의 값을 알기 위해서는 dp[1][1], dp[2][3], dp[1][2], dp[3][3]의 값을 밑에서 부터 알아야 하기 때문에 dp에 바텀업 방식으로 저장
            value = dp[j][k] + dp[k+1][i] + d[j-1] * d[k] * d[i]
            # k에 따른 분할에서 최적부분 행렬에 따른 최소값으로 갱신
            if answer > value:
                answer = value

            k += 1
            
            if k == i:
                break
        
        dp_re[j][i] = k-1
        # 위의 반복문에서 구한 최소값이 dp[j][i]의 값 즉 원하는 답
        dp[j][i] = answer

# dp[1][3]이 알고리즘에서 구하려는 최소값
print(dp[1][n])
order(dp_re, 1, n)
