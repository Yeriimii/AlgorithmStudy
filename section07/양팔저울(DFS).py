def DFS(L, sum):
    global res

    if L == n:
        if 0 < sum <= s:  # 대칭일 때 계산하지 않도록 양수일 때만, 합이 추의 합보다 작을 때만
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])  # 추를 왼쪽에 넣을 때
        DFS(L+1, sum-G[L])  # 추를 오른쪽에 넣을 때
        DFS(L+1, sum)  # 추를 사용하지 않을 때


if __name__ == '__main__':
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)  # 측정가능한 물의 무게
    res = set()  # 중복을 제거하며 값 추가
    DFS(0, 0)
    print(s - len(res))
