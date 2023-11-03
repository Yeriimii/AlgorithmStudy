n = int(input())
arr = [0] * 501
res = 0
for _ in range(n):
    index, value = map(int, input().split())
    arr[index] = value

dy = [0 for _ in range(501)]
for i in range(1, 501):
    if arr[i] > 0:
        dy[i] = 1
    else:
        continue
    maxx = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > maxx:
            maxx = dy[j]
        dy[i] = maxx + 1
        if dy[i] > res:
            res = dy[i]
if n > 1:
    print(n - max(dy))
elif n == 1:
    print(max(dy))
