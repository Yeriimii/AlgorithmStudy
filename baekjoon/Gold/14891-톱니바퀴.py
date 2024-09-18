def dfs(level: int, gear_idx: int, _direction: int):
    if level == 4 or 0 > gear_idx or 3 < gear_idx:
        return

    left = gear_idx - 1
    right = gear_idx + 1
    if gear_idx == 0:
        if gears[gear_idx][2] != gears[right][-2] and not visited[right]:
            visited[right] = True
            dfs(level + 1, right, -_direction)
            gears[right] = rotate(gears[right], -_direction)
    elif gear_idx == 3:
        if gears[gear_idx][-2] != gears[left][2] and not visited[left]:
            visited[left] = True
            dfs(level + 1, left, -_direction)
            gears[left] = rotate(gears[left], -_direction)
    elif gear_idx == 1 or gear_idx == 2:
        if gears[left][2] != gears[gear_idx][-2] and not visited[left]:
            visited[left] = True
            dfs(level + 1, left, -_direction)
            gears[left] = rotate(gears[left], -_direction)
        if gears[gear_idx][2] != gears[right][-2] and not visited[right]:
            visited[right] = True
            dfs(level + 1, right, -_direction)
            gears[right] = rotate(gears[right], -_direction)


def rotate(gear: str, _direction: int):
    if _direction == 1:
        return gear[7] + gear[:7]
    elif _direction == -1:
        return gear[1:] + gear[0]


if __name__ == '__main__':
    gears = [input() for _ in range(4)]
    state = [False for _ in range(3)]

    K = int(input())
    for _ in range(K):
        idx, direction = map(int, input().split())
        idx -= 1
        visited = [False for _ in range(4)]
        visited[idx] = True
        dfs(0, idx, direction)
        gears[idx] = rotate(gears[idx], direction)

    score = 0
    for i in range(4):
        if gears[i][0] == '1':
            score += 2 ** i
    print(score)
