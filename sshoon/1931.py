import sys

n = int(sys.stdin.readline())

times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = times[0][1]
for i in range(1, n):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]


print(cnt)

# [3, 5] [5, 7] [8, 11] [12, 14]
# [1, 4] [5, 7] [8, 11] [12, 14]

# [3, 5] [5, 7] [8, 12] [12, 14] 
# [1, 4] [5, 7] [8, 12] [12, 14]

# 1st time =>  [0 ,4]
# 2nd itme =>  [1, 5]
# 3rd time =>  [2, 6]
# 4th time =>  [3, 7]
# 5th time =>  [3, 8]
# 6th time =>  [5, 9]
# 7th time =>  [5, 10]
# 8th time =>  [6, 11]
# 9th time =>  [8, 12]
# 10th time => [8, 13]
# 11th time => [12, 14]

# -> [0, 4] [4, 7], [7, 11], [11, 12 13 14]
# -> [1, 4] [5, 7], [8, 11], [12, 14]