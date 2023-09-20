def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1  # pointer var
rt = largest  # pointer var
while lt <= rt:
    mid = (lt + rt) // 2  # 랜선의 길이
    if Count(mid) >= n:  # 답 가능성 있을 때
        res = mid
        lt = mid + 1
    else:  # 답이 아닐 때
        rt = mid - 1
print(res)
