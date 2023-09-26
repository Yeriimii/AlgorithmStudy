n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:  # 2 먼저 카운팅
        cnt += 1
        for j in range(i, n+1, i):  # 2의 배수 먼저 체크
            ch[j] = 1
print(cnt)
