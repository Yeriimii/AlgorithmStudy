import heapq as hq

a = list()
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))  # root node
    else:
        hq.heappush(a, -n)  # 부호를 반대로 -> 최대힙
