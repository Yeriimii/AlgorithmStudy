def dfs(l, w):
    global ans

    if w < 500:
        return
    if l == n:
        ans += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            dfs(l + 1, w - k + kits[i])
            visited[i] = False


n, k = map(int, input().split())
kits = list(map(int, input().split()))
visited = [False for _ in range(n)]
ans = 0
dfs(0, 500)
print(ans)
