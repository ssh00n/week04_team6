import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ranks = [list(map(int, input().split())) for _ in range(n)]
    ranks.sort()

    sa, sb = ranks[0]
    cnt = 1

    for rank in ranks[1:]:
        a, b = rank
        if sb >= b:
            cnt += 1
            sa, sb = a, b

    print(cnt)