import sys
from collections import deque

N = int(sys.stdin.readline())
flowers = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
flowers.sort()
queue = deque()
left = right = (3, 1)
max_right = (11, 30)
result = 0


# d1 = (월, 일)
def compare(d1, d2):  # d1 < d2 return 1, d1 == d2 return 0, d1 > d2 return -1
    if d1 == d2:
        # 같은 월/일
        return 0
    if d1[0] < d2[0] or (d1[0] == d2[0] and d1[1] < d2[1]):
        # d1이 d2보다 빠른 월이거나, d1과 d2가 같은 월일 때 d1의 일자가 더 빠른 날일 때
        return 1
    # d2가 d1보다 빠를 때
    return -1


for flower in flowers:
    m_1, d_1, m_2, d_2 = flower
    # 3월 1일보다 늦게 피는 꽃이 아니면
    if compare(left, (m_1, d_1)) != 1:
        # 11월 30일 보다 늦게 지는 꽃이면
        if compare(right, (m_2, d_2)) == 1:
            # right 갱신
            right = (m_2, d_2)
    # 3월 1일보다 일찍 피거나 3월에 피는 꽃이면
    elif compare(right, (m_1, d_1)) != 1:
        result += 1
        # left 갱신
        left = right
        if compare(right, (m_2, d_2)) == 1:
            right = (m_2, d_2)
    else:
        break
    if compare(max_right, right) == 1:  # 이미 11월 30을 넘어섰다면 종료
        result += 1
        break
if compare(max_right, right) == 1:
    print(result)
else:
    print(0)
