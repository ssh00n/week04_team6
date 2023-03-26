import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    
    n = int(input())

    # 서류심사 등수와 면접 등수를 저장할 리스트 생성
    people = []
    for _ in range(n):
        # 서류 심사 등수 면접 등수 리스트에 저장
        y, x = map(int, input().split())
        people.append((y,x))

    # 처음 서류 심사 등수로 정렬
    people.sort()
    

    # 그리디 알고리즘으로 이미 서류심사 등수는 오름차순으로 정렬되어있기 때문에 면접등수도 작다면 합격 할수 없다.
    first = people[0][1]
    count_ = 1
    
    for i in range(1, n):
        # 그러므로 면접등수는 서류심사 1등 등수보다 작아야 한다.
        if people[i][1] < first:
            # 작다면 카운트를 늘려 준다
            count_ += 1
            # 순서에 의해 면접등수를 다음 시험 등수가 높은 사람으로 초기화
            first = people[i][1]
    
    print(count_)
   
            