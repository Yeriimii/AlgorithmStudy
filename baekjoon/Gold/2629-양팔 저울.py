def DFS(L, sum):
    global res

    new = abs(sum)
    res.add(new)

    if L == n:
        return 0
    else:
        if dp[L][new] == 0:
            DFS(L + 1, sum + G[L])  # 추를 왼쪽에 넣을 때
            DFS(L + 1, sum - G[L])  # 추를 오른쪽에 넣을 때
            DFS(L + 1, sum)  # 추를 사용하지 않을 때
            dp[L][new] = 1


if __name__ == '__main__':
    n = int(input())
    G = list(map(int, input().split()))
    bn = int(input())
    beads = list(map(int, input().split()))

    # dp[i][j] = i번째 까지의 추를 놓았을 때 j 무게를 만들 수 있는지
    dp = [[0] * (30 * 500 + 1) for _ in range(n + 1)]
    res = set()  # 중복을 제거하며 값 추가

    DFS(0, 0)

    for idx, x in enumerate(beads):
        if x in res:
            print("Y", end=' ')
        else:
            print("N", end=' ')
