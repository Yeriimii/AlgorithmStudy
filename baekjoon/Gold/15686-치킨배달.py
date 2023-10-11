def DFS(L, s):
    global res
    if L == m:
        sum = 0  # 도시의 치킨 거리
        for j in range(len(home)):
            x1 = home[j][0]
            y1 = home[j][1]
            dis = 2147000000
            for x in cb:
                x2 = shop[x][0]
                y2 = shop[x][1]
                dis = min(dis, abs(x2-x1) + abs(y2-y1))
            sum += dis  # 집 마다 치킨 거리의 최소값의 합 = 도시의 치킨 거리

        if sum < res:
            res = sum

    else:
        for i in range(s, len(shop)):
            cb[L] = i  # i 번째 치킨집을 선택했을 때(폐업 아님)
            DFS(L+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    shop = list()
    home = list()
    board = [list(map(int, input().split())) for _ in range(n)]
    cb = [0] * m  # 치킨 집 조합
    res = 2147000000
    for k in range(n):
        for l in range(n):
            if board[k][l] == 1:
                home.append((k, l))
            elif board[k][l] == 2:
                shop.append((k, l))
    DFS(0, 0)
    print(res)
