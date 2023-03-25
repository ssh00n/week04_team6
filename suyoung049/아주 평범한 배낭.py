import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline


n, k = map(int, input().split())
# 배낭에 배열 순서를 늘려주기 위해 빈 데이터 추가
bag = [(0,0)]

# 점화식을 위한 이차원 배열 array 생성
dp = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    # 가방에 들어갈 무게랑 가치 설정
    weight, value = map(int, input().split())

    # 가방에 들어갈 물건을 반복해서 넣어주기
    bag.append((weight, value))

# 열은 물건의 순서
for i in range(1, n+1):
    # 행은 무게의 제한을 range로 순차적으로 나열
    for limit in range(1, k+1):
        # 인덱스 별로 물건의 무게, 가치 설정
        weight, value = bag[i]

        # 현재 물건이 현재 인덱스보다 작다면 바로 [이전 물건][같은 무게] dp[i-1][limit]를 입력
        if limit < weight:
            dp[i][limit] = dp[i-1][limit]
        
        # 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최대값(dp[i-1][limit-weight]을 위의 행에서 가져와 value에 더해준다)
        # 현재 물건을 넣어주는 것 보다 다른 물건들로 채우는 값 (dp[i-1][limit])을 가져온다
        # 두 물건중에 큰 값이 그 무게의 최대 value (max(dp[i-1][limit], dp[i-1][limit-weight] + value))
        else:
            dp[i][limit] = max(dp[i-1][limit], dp[i-1][limit-weight] + value)

# dp에서 물건의 개수, 만들 수 있는 가치 만큼 데이터 출력
print(dp[n][k])