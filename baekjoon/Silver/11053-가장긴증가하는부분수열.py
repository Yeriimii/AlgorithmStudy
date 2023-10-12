n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n+1)
dy[0] = 1
dy[1] = 1
res = 0
for i in range(1, n+1):
    max_len = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and max_len < dy[j]:
            max_len = dy[j]
    dy[i] = max_len + 1
    res = max(dy[i], res)
print(res)
