def dfs(L: int, used: int, S: int, B: int):
    global answer
    if L == n:
        if used != 0:
            answer = min(answer, abs(S - B))
        return

    dfs(L + 1, used + 1, S * arr[L][0], B + arr[L][1])
    dfs(L + 1, used, S, B)


if __name__ == '__main__':
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    answer = 1000000000
    dfs(0, 0, 1, 0)
    print(answer)
