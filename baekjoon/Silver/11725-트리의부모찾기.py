# import sys
#
# sys.setrecursionlimit(10**6)
#
# def DFS(tree, node, visited):
#     visited[node] = 1
#     for x in tree[node]:
#         if not visited[x]:
#             res[x] = node
#             DFS(tree, x, visited)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     visited = [False] * (n+1)
#     tree = [[] for _ in range(n+1)]
#     res = [0] * (n + 1)
#     for _ in range(n - 1):
#         node_a, node_b = map(int, sys.stdin.readline().split())
#         tree[node_a].append(node_b)
#         tree[node_b].append(node_a)
#
#     DFS(tree, 1, visited)
#
#     for i in range(2, n+1):
#         print(res[i])

from collections import deque

n = int(input())
visited = [False] * (n + 1)
answer = [0] * (n + 1)
tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)


def bfs(tree, node, visited):
    Q = deque([node])
    visited[node] = True
    while Q:
        x = Q.popleft()
        for i in tree[x]:
            if not visited[i]:
                answer[i] = x
                Q.append(i)
                visited[i] = True


bfs(tree, 1, visited)

for i in range(2, n + 1):
    print(answer[i])


