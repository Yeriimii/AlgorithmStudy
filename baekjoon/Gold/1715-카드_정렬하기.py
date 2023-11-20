import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list()
for _ in range(n):
    x = int(input())
    heapq.heappush(numbers, x)

res = 0
tmp = []
while numbers:
    pop_x = heapq.heappop(numbers)
    tmp.append(pop_x)
    if len(tmp) == 2:
        res += sum(tmp)
        heapq.heappush(numbers, sum(tmp))
        tmp.clear()
print(res)
