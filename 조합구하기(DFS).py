def DFS(L, s):
    global cnt

    if L == m:  # 중단점
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):  # 1 부터 시작
            res[L] = i
            DFS(L+1, i+1)  # 다음 재귀부터 1+1=2부터 시작


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
