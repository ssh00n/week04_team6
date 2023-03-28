# 1946. 신입사원
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    candidates = []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        # if x == 1:
        #     target_y = y
        # if y == 1:
        #     target_x = x
        candidates.append([x, y])
    candidates.sort()
    
    target_y = candidates[0][1]
    cnt = 0
    for candidate in candidates:
        if candidate == candidates[0]:
            cnt += 1
        elif candidate[1] < target_y:
            cnt += 1
            target_y = candidate[1]
            
    print(cnt)


# 1 2
# 2 1 


# x 기준으로 오름차순 정렬 -> y_target 저장
# 아래 원소들이 y_target보다 작다면 다 합격

# [1, 4]
# [4, 2]
# [6, 1]

# [6, 4] 보다 모두 작은 수