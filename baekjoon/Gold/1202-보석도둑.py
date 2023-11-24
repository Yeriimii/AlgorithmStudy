import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewelry.sort()
bags.sort()

tmp_bag = list()
res = 0
for bag in bags:
    while jewelry:
        if jewelry[0][0] <= bag:
            heapq.heappush(tmp_bag, -jewelry[0][1])
            heapq.heappop(jewelry)
        else:
            break

    if tmp_bag:
        res += -heapq.heappop(tmp_bag)

print(res)
