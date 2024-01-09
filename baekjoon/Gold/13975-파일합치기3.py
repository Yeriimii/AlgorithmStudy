import heapq

T = int(input())
origin = []
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    heapq.heapify(pages)
    res = 0
    while len(pages) > 1:
        a = heapq.heappop(pages)
        b = heapq.heappop(pages)
        res += a + b
        heapq.heappush(pages, a + b)
    print(res)
