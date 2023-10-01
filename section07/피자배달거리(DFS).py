def DFS(L, s):
    global res

    if L == m:
        sum = 0  # 도시의 피자 거리
        for j in range(len(hs)):  # 집의 개수 만큼 루프
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))  # dis 최소값 갱신
            sum += dis  # 도시의 피자 배달 거리
        if sum < res:
            res = sum

    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pz = list()
    hs = list()
    cb = [0] * m  # combination
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                pz.append((i, j))
            elif board[i][j] == 1:
                hs.append((i, j))
    DFS(0, 0)
    print(res)
