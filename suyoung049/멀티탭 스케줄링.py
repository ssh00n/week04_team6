import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# 1.사용할 플러그가 이미 꽂혀 있으면 continue
# 2. 플러그를 꽂을 자리가 있다면 append 해주고 continue
# 3. 플러그를 뽑아야 하는 상황이라면
#    - 꽂혀 있는 플러그를 하나씩 확인한다.
#    - 해당 플러그가 추후 사용해야할 플러그 중에 없으면 그자리를 현재 사용할 플러그로 업데이트
#    - 만약 추후 사용해야 할 플러그라면 가장 마지막에 사용할 플러그의 인덱스를 구해서 현재 사용할 플러그로 업데이트
#    - 그리디 알고리즘에 의해 가장 마지막에 사용할 플러그를 교체해야지 교체할 최소카운드틀 구할 수 있다.

# 플러그를 꽂을 수 있는 공간의 수, 장비의 수 지정
plug_count, equipment = map(int, input().split())

# 장비의 번호에 따른 사용 순서 리스트로 저장
use_number = list(map(int, input().split()))

# 현재 꽂혀 있는 장비 리스트
plug_li = []

# 플러그를 빼는 수
count_ = 0

# 장비의 리스트에서 반복문 시작
for i in range(equipment):
    # 현재 꽂혀 있는 장비의 순서라면 continue
    if use_number[i] in plug_li:
        continue
    # 플러그를 꽂을 공간이 남아있다면 plug_li에 append
    elif len(plug_li) != plug_count:
        plug_li.append(use_number[i])

    # 위의 두가지 상황이 아니라면 플러그를 빼야 하는 상황이다.
    else:
        # 꽂혀 있는 장비가 남아 있는 장비순서에 없거나, 가장 뒤의 순서의 장비일 경우 인덱스를 저장하기 위한 임시 temp  
        temp = 0
        # 가장 멀리 있는 장비를 알기위한 인덱스 초기화
        far_node = 0

        for plug in plug_li:
            # 남아있는 장비 순서에 꽂혀있는 장비가 없다면 바로 교체 
            if plug not in use_number[i:]:
                # 위의 장비의 위치에 다음 장비를 꽂아야 하기 때문에 인덱스 temp에 저장
                idx = plug_li.index(plug)
                temp = idx
                # 남아있는 장비 순서에 없는 장비가 교체 우선순위가 가장 높기 때문에 바로 반복문 종료
                break
            
            else:
                # 꽂혀있는 장비 모두 남아있는 장비순서에 있다면 그리디 알고리즘에 의해 가장 뒤 순서에 있는 장비의 플러그를 교체해준다.
                idx = use_number[i:].index(plug)
                # 플러그에 꽂혀있는 장비의 순서를 반복문을 돌리면서 가장 늦은 순서로 저장
                if far_node < idx:
                    # far_node에 저장 된 인덱스보다 뒤에 있는 인덱스가 나올 때마다 뒤에 있는 인덱스로 초기화
                    far_node = idx
                    # 가장 뒤 순서에 있는 장비의 플러그에 꽂혀 있는 인덱스를 temp에 저장 
                    idx_2 = plug_li.index(use_number[i:][far_node])
                    temp = idx_2
        
        # 플러그를 빼야 하는 상황에 맞게 최종 temp의 위치에 플러그를 교체
        plug_li[temp] = use_number[i]
        # 플러그를 교체해 줄 때마다 카운트 증가
        count_ += 1
        
print(count_)
    


