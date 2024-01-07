import heapq


def extract(heap):
    global M

    cnt = 1
    while heap:
        if cnt == M:
            return
        heapq.heappop(heap)
        cnt += 1


def sum_res(a):
    global flag, res

    if not flag:
        flag = True
        res += a
    else:
        res += a * 2


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

plus_max_heap = []
minus_max_heap = []
for x in numbers:
    if x < 0:
        heapq.heappush(minus_max_heap, x)
    elif x > 0:
        heapq.heappush(plus_max_heap, -x)

res = 0
flag = False
while minus_max_heap or plus_max_heap:
    plus_v = None
    minus_v = None

    if plus_max_heap:
        plus_v = -heapq.heappop(plus_max_heap)

    if minus_max_heap:
        minus_v = -heapq.heappop(minus_max_heap)

    if plus_v is not None and minus_v is not None:
        if not flag:
            flag = True
            if plus_v >= minus_v:
                res += plus_v
                heapq.heappush(minus_max_heap, -minus_v)
                extract(plus_max_heap)
            elif plus_v < minus_v:
                res += minus_v
                heapq.heappush(plus_max_heap, -plus_v)
                extract(minus_max_heap)
        else:
            if plus_v >= minus_v:
                res += plus_v * 2
                heapq.heappush(minus_max_heap, -minus_v)
                extract(plus_max_heap)
            elif plus_v < minus_v:
                res += minus_v * 2
                heapq.heappush(plus_max_heap, -plus_v)
                extract(minus_max_heap)
    elif plus_v is None and minus_v is not None:
        sum_res(minus_v)
        extract(minus_max_heap)
    elif plus_v is not None and minus_v is None:
        sum_res(plus_v)
        extract(plus_max_heap)
print(res)
