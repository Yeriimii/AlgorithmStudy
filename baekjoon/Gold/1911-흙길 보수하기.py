import sys

input = sys.stdin.readline


def count(sub):
    global L
    if sub <= 0:
        return 0
    quotient = sub // L
    if quotient > 0:
        remainder = sub % L
        if remainder > 0:
            return quotient + 1
        else:
            return quotient
    else:
        return 1


N, L = map(int, input().rstrip().split())
pools = [list(map(int, input().rstrip().split())) for _ in range(N)]
pools.sort()

prev_s, prev_e = 0, 0
res = 0
for pool in pools:
    s, e = pool[0], pool[1]
    if prev_e > s:
        s = prev_e
    subtract = e - s
    cnt = count(subtract)
    res += cnt
    prev_e = s + L * cnt
print(res)
