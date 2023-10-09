import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dy = [[0]*3 for _ in range(n)]
dy[0][0] = house[0][0]
dy[0][1] = house[0][1]
dy[0][2] = house[0][2]
for i in range(n):
    dy[i][0] = min(dy[i-1][1], dy[i-1][2]) + house[i][0]
    dy[i][1] = min(dy[i-1][0], dy[i-1][2]) + house[i][1]
    dy[i][2] = min(dy[i-1][0], dy[i-1][1]) + house[i][2]
print(min(dy[n-1]))
