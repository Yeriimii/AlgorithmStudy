n = int(input())
dy = [0] * (n+3)
dy[2] = 1
dy[3] = 1
if 1 <= n < 4:
    print(dy[n])
else:
    for i in range(4, n+1):
        if i % 3 == 0 and i % 2 == 0:
            dy[i] = min(dy[i//3] + 1, dy[i//2] + 1, dy[i-1] + 1)
        elif i % 3 == 0:
            dy[i] = min(dy[i//3] + 1, dy[i-1] + 1)
        elif i % 2 == 0:
            dy[i] = min(dy[i//2] + 1, dy[i-1] + 1)
        else:
            dy[i] = dy[i-1] + 1
    print(dy[n])




