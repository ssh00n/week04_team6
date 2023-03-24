import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

# 동전의 종류를 담을 리스트
coin_li = []

for _ in range(n):
    # 동전의 종류
    coin = int(input())
    coin_li.append(coin)

# 최소의 동전개수를 구하기 위해서 내림차순으로 변경
coin_li = sorted(coin_li, reverse=True)

count_ = 0
for money in coin_li:
    # 내림차순으로 정렬 했기 때문에 구해야 하는 값보다 작거나 같은 코인으로 시작
    if money <= k:
        # 몫은 동전의 개수
        count_ += k//money
        # 나머지는 다시 구해야 할 값
        k %= money

        if k == 0:
            break

print(count_)
        