def DFS(L):
    global cnt

    if L == m:  # 중단점 설정
        for j in res:
            print(j, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1  # 상태 체크
                res[L] = i  # 값 저장
                DFS(L+1)
                ch[i] = 0  # 상태 체크 반환


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)  # 백트래킹을 위한 상태체크 리스트
    cnt = 0
    DFS(0)
    print(cnt)
