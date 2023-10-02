n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:  # 마지막 항인 i의 앞의 숫자보다 마지막 항인 i가 클 때 최대길이 찾기
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]
print(res)



