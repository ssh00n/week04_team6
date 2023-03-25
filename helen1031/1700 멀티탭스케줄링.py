import sys
input = sys.stdin.readline

from collections import deque
import heapq

n, k = map(int, input().split())
devices = deque(list(map(int, input().split())))
ddict = {}
for device in devices:
    if device not in ddict:
        ddict[device] = 1
    else:
        ddict[device] += 1

plugs = set()

cnt = 0
while devices:
    current = devices.popleft()
    ddict[current] -= 1

    if len(plugs) < n:
        plugs.add(current)
    else:
        if current in plugs:
            continue
        else:
            # 무엇을 선택하느냐 그것이 문제로다
            # devices 중에서 앞으로 나올 일이 없는걸 뽑는다
            # 다 나온다면 devices 중에서 가장 나중에 꽂는 제품을 찾는다
            out = 0
            idxchk = []
            for plug in plugs:
                if ddict[plug] == 0:
                    out = plug
                    break
                else:
                    heapq.heappush(idxchk, (-devices.index(plug), plug))

            if out == 0:
                idx, out = heapq.heappop(idxchk)

            plugs.remove(out)
            plugs.add(current)
            cnt += 1

print(cnt)