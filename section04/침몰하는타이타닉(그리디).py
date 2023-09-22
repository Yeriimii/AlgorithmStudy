from collections import deque

'''
deque는 list와 달리 pop 연산 후 재정렬하지 않는다.
'''
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break

    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    elif p[0] + p[-1] <= limit:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)
