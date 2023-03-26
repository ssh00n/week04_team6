import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

# 회의실 대여 시작시간과 끝시간 저장할 리스트
room_li = []
for _ in range(n):
    # 시작 시간 끝 시간 추가
    start, end = map(int, input().split())
    room_li.append((start, end))


# 데이터 정렬을 (끝나는 시간, 시작 시간) 순으로 정렬
room_li = sorted(room_li, key= lambda x:(x[1],x[0]))

# 그리디 알고리즘으로 해결하기 위해 앞 대여시간의 끝 시간 보다 다음 대여시간이 큰 시간중에 가장 큰시간을 가져오기 위해 정렬
# (1,4),(5,7)(8,11)(12,14) 순으로 정렬 하기 위해

count_ = 1

for i in range(n):
    if i == 0:
        start_time = room_li[i][1]
    
    elif room_li[i][0] >= start_time:
        # 위의 정의에 따라 끝시간보다 시작시간이 작거나 같다면 횟수 증가 
        count_ += 1
        # 처음 정의 해준 끝시간 다음 대여시간의 끝시간으로 초기화
        start_time = room_li[i][1]

print(count_)
