import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x:(x[1], x[0]))
print(meetings)

cstart, cend = meetings[0]
cnt = 1

for i, meeting in enumerate(meetings[1:]):
    start, end = meeting
    if cend > start:
        continue
    else:
        cnt += 1
        cstart, cend = start, end
print(cnt)