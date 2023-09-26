a = input()
res = 0
for x in a:
    if x.isdecimal():
       res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):  # 약수 개수 카운팅
    if res % i == 0:
        cnt += 1
print(cnt)
