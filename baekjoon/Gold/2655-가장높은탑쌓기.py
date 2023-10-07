import sys

n = int(sys.stdin.readline())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())  # (너비, 높이, 무게)
    bricks.append((a, b, c, i+1))
bricks.sort(reverse=True)  # 너비 순으로 역순 정렬

res2 = 0
dy = [0] * n  # dynamic 테이블 (높이)
dy2 = [0] * n  # dynamic 테이블 (개수)
dy3 = [[0]] * n
dy[0] = bricks[0][1]  # 0 번째 벽돌의 높이
res = bricks[0][1]  # 0 번째 벽돌의 높이
dy2[0] = 1
dy3[0] = [bricks[0][3]]
for i in range(1, n):  # dynamic 테이블 순회하며 값 채우기
    max_h = 0
    max_b = 0
    brick_num = None
    for j in range(i-1, -1, -1):  # bricks 역순회
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:  # 이전 벽돌 무게 > 다음 벽돌 무게 조건 검사
            max_h = dy[j]  # 최대 높이 갱신
            max_b = dy2[j]
            brick_num = dy3[j]
    dy[i] = max_h + bricks[i][1]  # dy[현재 벽돌] 높이 갱신
    dy2[i] = max_b + 1
    if brick_num is not None:
        dy3[i] = [bricks[i][3]] + brick_num
    else:
        dy3[i] = [bricks[i][3]]
    res = max(res, dy[i])  # 전체 높이 최대값 갱신
    res2 = dy2[dy.index(res)]
print(res2)
while dy3[dy.index(res)]:
    print(dy3[dy.index(res)].pop(0))
