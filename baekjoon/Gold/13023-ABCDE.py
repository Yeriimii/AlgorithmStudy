def dfs(start_node, cnt):
    global res

    visited[start_node] = True

    if res == 1 or cnt == 5:
        res = 1
        return
    else:
        for next_node in elist[start_node]:
            if not visited[next_node]:
                dfs(next_node, cnt + 1)
                visited[next_node] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    elist = [[] for _ in range(n+1)]
    for _ in range(m):
        start_node, end_node = map(int, input().split())
        elist[start_node].append(end_node)
        elist[end_node].append(start_node)

    res = 0
    for node in range(n):
        visited = [False] * (n + 1)
        if len(elist[node]) > 0:
            dfs(node, 1)
            if res == 1:
                break
    print(res)
