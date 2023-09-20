def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:  # Music 탐색
        if sum + x > capacity:  # 저장용량 초과하면
            cnt += 1  # DVD 1장 추가
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
Music = list(map(int, input().split()))
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
