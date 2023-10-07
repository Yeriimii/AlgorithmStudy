n, m = map(int, input().split())
if n == 1:
    n += 1
ch = [0] * (m+1)
for i in range(2, m+1):
    if ch[i] == 0:  # 2 먼저 카운팅
        if i >= n:
            print(i)
        for j in range(i, m+1, i):  # 2의 배수 먼저 체크
            ch[j] = 1
