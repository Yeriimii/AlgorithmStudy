"""
크루스칼 알고리즘(union-find) : 간선이 적을 때 최소 신장 트리(MST, 최소 스패닝 트리)를 구하는 방법
"""

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
parent = list(range(n + 1))


def find(parent, x):
    if parent[x] != x:
        # x의 부모를 갱신한다.
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    # 둘 중 작은 값이 부모가 된다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
res = 0
for i in range(n):
    star_1 = stars[i]
    x1, y1 = star_1[0], star_1[1]
    for j in range(i + 1, n):
        star_2 = stars[j]
        x2, y2 = star_2[0], star_2[1]
        cost = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
        edges.append((cost, i, j))

edges.sort()
for i in range(len(edges)):
    cost, star1, star2 = edges[i]
    if find(parent, star1) != find(parent, star2):
        union(parent, star1, star2)
        res += cost

print(res)
