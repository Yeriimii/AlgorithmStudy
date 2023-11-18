import sys
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().split())
monster_room = []
weapon_room = []

for _ in range(n):
    room, stat = map(int, input().split())
    if room == 1:
        monster_room.append(stat)
    else:
        weapon_room.append(stat)

monster_room.sort()
weapon_room.sort()
Q1 = deque(monster_room)
Q2 = deque(weapon_room)

res = 0
while Q1:

    stat = Q1.popleft()

    if stat < d:
        d += stat
        res += 1
    else:
        Q1.appendleft(stat)
        if Q2:
            d *= Q2.popleft()
            res += 1
        else:
            break
while Q2:
    stat = Q2.popleft()
    res += 1

print(res)
