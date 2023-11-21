# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence
from collections import deque

str1 = input()
str2 = input()
str1 = ' ' + str1
str2 = ' ' + str2
str1_len = len(str1)
str2_len = len(str2)
LCS = [[0] * str1_len for _ in range(str2_len)]

for i in range(str2_len):
    for j in range(str1_len):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str2[i] == str1[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

result = list()

start = LCS[str2_len - 1][str1_len - 1]

Q = deque()
Q.append((str2_len - 1, str1_len - 1))
dx = [-1, 0]
dy = [0, -1]
while Q:
    x, y = Q.popleft()
    if x == 0 or y == 0:
        break

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and 0 <= ny and LCS[nx][ny] == LCS[x][y]:
            Q.append((nx, ny))
            break
    else:
        result.append(str2[x])
        Q.append((x - 1, y - 1))

print(LCS[str2_len-1][str1_len-1])
result.reverse()
for x in result:
    print(x, end='')