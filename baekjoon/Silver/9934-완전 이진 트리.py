def dfs(level: int, start: int, end: int):
    if start > end:
        return
    mid = (start + end) // 2
    q[level].append(visit[mid])  # root
    dfs(level + 1, start, mid - 1)  # left
    dfs(level + 1, mid + 1, end)  # right


if __name__ == '__main__':
    K = int(input())
    visit = list(map(int, input().split()))
    q = [[] for _ in range(K)]
    dfs(0, 0, len(visit) - 1)

    for levels in q:
        for node in levels:
            print(node, end=' ')
        print()
