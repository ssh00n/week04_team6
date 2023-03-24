import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

# 최소값을 구하기 위해서는 '-'를 이용해서 쪼개기
result = input().split('-')

for i in range(len(result)):
    # '-'를 기준으로 쪼갠 수 다시 '+' 기준으로 쪼개기
    sum_ = map(int, result[i].split('+'))

    # 첫번째수는 정답에 무조건 더하기
    if i == 0:
        answer = sum(sum_)
    
    # 다음수부터는 빼주면 최소값을 구할 수 있다.
    else:
        answer -= sum(sum_)



print(answer)