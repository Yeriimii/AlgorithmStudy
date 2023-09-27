def DFS(L, sum, time):
    global res

    if time > m:  # 시간 초과시 중단
        return

    if L == n:  # 말단 노드에 도착 했을 때
        if sum > res:
            res = sum
    else:  # 뻗어 나갔을 때
        DFS(L+1, sum + pv[L], time + pt[L])  # 문제를 푼다
        DFS(L+1, sum, time)  # 문제를 안푼다


if __name__ == '__main__':
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)  # 점수
        pt.append(b)  # 시간
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
