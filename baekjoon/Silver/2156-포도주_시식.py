n = int(input())
num = list()
num.append(0)
for _ in range(n):
    num.append(int(input()))
res = 0
dy = [0] * (n+1)
dy[1] = num[1]
if n >= 3:
    dy[2] = num[1] + num[2]
    for i in range(3, n+1):
        dy[i] = num[i] + max(num[i-1] + max(dy[:i-2]), max(dy[:i-1]))
elif n == 1:
    dy[1] = num[1]
elif n == 2:
    dy[2] = num[1] + num[2]
print(max(dy))
