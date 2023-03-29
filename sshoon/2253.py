import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[] for _ in range(n+1)]
too_small = set()
for _ in range(m):
    too_small.add(int(input()))


def bfs():
    if n == 2:
        return 1
    else:
        start = 1
        if 2 in too_small:
            return -1
        
        start += 1
        last_jump = 1
        cur_count = 1
        q = deque()
        q.append((start, last_jump, cur_count))

        while q:
            cur_stone, last_jump, cur_count= q.popleft()
            if cur_stone == n:
                return cur_count
                
            
            dx = [last_jump-1, last_jump, last_jump+1]
            for i in range(3):
                if dx[i] > 0 and cur_stone+dx[i] in range(n+1):
                    nx = cur_stone + dx[i]
                    if nx not in too_small and dx[i] not in visited[nx]:
                        visited[nx].append(dx[i])
                        q.append((nx, dx[i], cur_count+1))
        
        return -1

print(bfs())
            
        


