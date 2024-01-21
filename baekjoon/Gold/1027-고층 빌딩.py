N = int(input())
buildings = list(map(int, input().split()))
for i in range(N):
    buildings[i] = (i, buildings[i])
res = 0
INF = float('inf')
LEFT = -1
RIGHT = 1


def calculate_inclination(this, other):
    x1, y1 = this[0], this[1]
    x2, y2 = other[0], other[1]
    if x2 - x1 != 0:
        return 1.0 * ((y2 - y1) / (x2 - x1))


def dfs(index, next_index, last_visible_inclination):
    global visible_building_cnt
    if next_index == N or next_index == -1:
        return

    new_inclination = calculate_inclination(buildings[index], buildings[next_index])

    if next_index > index:
        if last_visible_inclination == INF or new_inclination > last_visible_inclination:
            visible_building_cnt += 1
            last_visible_inclination = new_inclination
        dfs(index, next_index + RIGHT, last_visible_inclination)
    elif next_index < index:
        if last_visible_inclination == INF or last_visible_inclination > new_inclination:
            visible_building_cnt += 1
            last_visible_inclination = new_inclination
        dfs(index, next_index + LEFT, last_visible_inclination)


for idx in range(N):
    visible_building_cnt = 0
    # left
    if idx >= 1:
        dfs(idx, idx - 1, INF)
    # right
    if idx <= N - 2:
        dfs(idx, idx + 1, INF)
    res = max(res, visible_building_cnt)
print(res)
