n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
cnt = 0
for x in a:
    if k == 0:
        break
    if k // x >= 1:
        cnt += (k // x)
        k = k % x
print(cnt)
