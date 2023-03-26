import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

# 인덱스 1부터 시작하기 위해 두 문장을 리스트에 넣기 전에 먼저 공백을 앞에 지정해준다.
first_sentence = [' '] + list(input().strip())
second_sentence = [' '] + list(input().strip())

# 공백을 포함한 문자의 길이를 선언
m, n = len(first_sentence), len(second_sentence)

# 최장 공통 부분 수열의 길이를 저장하기 위한 2차원 배열 선언
dp = [[0] * n for _ in range(m)]

# 문장의 앞 부분에는 공백이 있으므로 1부터 시작 바텀업 방식으로 구현
for j in range(1, m):
    for i in range(1, n):

        # 두 문장 인덱스의 단어가 같지 않다면 두 문장 전 인덱스의 공동 부분 수열의 길이중 큰 값을 가져온다.
        if first_sentence[j] != second_sentence[i]:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        # 두 문장의 배열의 단어가 같다면, 전 인덱스의 공통 부분 수열의 길이에 1을 더해준다.
        elif first_sentence[j] == second_sentence[i]:
            dp[j][i] = dp[j-1][i-1] + 1



print(dp[m-1][n-1])