import sys

input = sys.stdin.readline

# 입력 전처리 - 숫자와 기호 분리
s = input().rstrip()
operands = []
for c in s:
    if c in ('-', '+'):
        operands.append(c)
s = s.replace("+", " ")
s = s.replace("-", " ")
nums = list(map(int, s.split()))

# a - b 구조 -> b를 최대로 만들고, 맨 마지막에 a - b 연산을 수행한다
a = nums[0]
b = 0
nums = nums[1:]

for i, operand in enumerate(operands):
    if operand == '+':
        if b == 0:
            a += nums[i]
        else: # - 연산이 이미 기존에 존재하기에 b를 최대로 만들기 위해 b에 더하기 수행
            b += nums[i]
    else:
        if b == 0:
            b += nums[i]
        else: # b 깂이 작아지는 것을 방지하기 위해 중간 연산 후 b 값 대체
            a = a - b
            b = nums[i]

print(a - b)