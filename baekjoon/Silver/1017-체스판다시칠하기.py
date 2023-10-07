n, m = map(int, input().split())
board = [input() for _ in range(n)]
res = 2147000000
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0  # 맨 왼쪽 위가 W 일 때
        cnt2 = 0  # 맨 왼쪽 위가 B 일 때
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:  # 홀수 번째만 계산
                    if board[i + k][j + l] != 'W':  # 맨 왼쪽 위가 W인데, 홀수 번째가 W가 아닐 떄
                        cnt1 += 1
                    if board[i + k][j + l] != 'B':  # 맨 왼쪽 위가 B인데, 홀수 번째가 B가 아닐 대
                        cnt2 += 1
                else:  # 짝수 번째만 계산
                    if board[i + k][j + l] != 'B':  # 맨 왼쪽 위가 W인데, 짝수 번째가 B가 아닐 떄
                        cnt1 += 1
                    if board[i + k][j + l] != 'W':  # 맨 왼쪽 위가 W인데, 짝수 번째가 W가 아닐 떄
                        cnt2 += 1
        res = min(res, cnt1, cnt2)
print(res)
