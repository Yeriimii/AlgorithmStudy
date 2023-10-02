n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())  # (너비, 높이, 무게)
    bricks.append((a, b, c))
bricks.sort(reverse=True)  # 너비 순으로 역순 정렬
dy = [0] * n  # dynamic 테이블
dy[0] = bricks[0][1]  # 0 번째 벽돌의 높이
res = bricks[0][1]  # 0 번째 벽돌의 높이
for i in range(1, n):  # dynamic 테이블 순회하며 값 채우기
    max_h = 0
    for j in range(i-1, -1, -1):  # bricks 역순회
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:  # 이전 벽돌 무게 > 다음 벽돌 무게 조건 검사
            max_h = dy[j]  # 최대 높이 갱신
    dy[i] = max_h + bricks[i][1]  # dy[현재 벽돌] 높이 갱신
    res = max(res, dy[i])  # 전체 높이 최대값 갱신
print(res)