import heapq as hq
import sys

n = int(sys.stdin.readline())
a = list()
b = list()
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp != 0:
        if tmp < 0:
            hq.heappush(b, -tmp)
        else:
            hq.heappush(a, tmp)
    elif tmp == 0:
        if len(a) == 0 and len(b) == 0:
            print(0)
        elif len(a) > 0 and len(b) == 0:
            left = hq.heappop(a)
            print(left)
        elif len(b) > 0 and len(a) == 0:
            right = hq.heappop(b)
            print(-right)
        else:
            left = hq.heappop(a)
            right = hq.heappop(b)
            if left == right:
                print(-right)
                hq.heappush(a, left)
            elif left > right:
                print(-right)
                hq.heappush(a, left)
            elif left < right:
                print(left)
                hq.heappush(b, right)
