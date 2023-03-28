import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

schedule = list(map(int, input().split()))

d = {}
for s in schedule:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

heap = []

print(d)
unplug = 0

for i in range(len(schedule)):
    temp = {}
    
    if len(heap) < n:
        if (d[schedule[i]], schedule[i]) in heap:
            heap.remove((d[schedule[i]], schedule[i]))
            heapq.heappush(heap, (d[schedule[i]]-1, schedule[i]))
            heapq.heapify(heap)
            temp[schedule[i]] = d[schedule[i]] - 1
            d.update(temp)
            print(d[schedule[i]], schedule[i])
            
        else:
            heapq.heappush(heap, (d[schedule[i]]-1, schedule[i]))
            temp[schedule[i]] = d[schedule[i]] - 1
            d.update(temp)
            print(d[schedule[i]], schedule[i])
        
    else:
        if (d[schedule[i]], schedule[i]) in heap:
            heap.remove((d[schedule[i]], schedule[i]))
            heapq.heappush(heap, (d[schedule[i]]-1, schedule[i]))
            heapq.heapify(heap)
            temp[schedule[i]] = d[schedule[i]] - 1
            d.update(temp)
            print(d[schedule[i]], schedule[i])

        else:
            top_key, top_value = heap[0][0], heap[0][1]
            bottom_key, bottom_value = heap[-1][0], heap[-1][1]
            
            if schedule[i:i+n].count(top_value) > schedule[i:i+n].count(bottom_value):
                print(f"{heap[-1]} unplugged")
                heap.remove(heap[-1])
                heapq.heappush(heap, (d[schedule[i]]-1, schedule[i]))
                heapq.heapify(heap)
                temp[schedule[i]] = d[schedule[i]] - 1
                d.update(temp)
                unplug += 1
                
            else:
                p, v = heapq.heappop(heap)
                print(f"{p} {v} unplugged")
                heapq.heappush(heap, (d[schedule[i]]-1, schedule[i]))
                temp[schedule[i]] = d[schedule[i]] - 1
                d.update(temp)
                unplug += 1
                print(d[schedule[i]], schedule[i])
    print(d)
    print(heap)
    
print(unplug)
