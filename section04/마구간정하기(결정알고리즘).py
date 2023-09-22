def Count(len):
    cnt = 1  # 1마리 배치(맨 왼쪽에 배치)
    ep = Line[0]  # 엔드포인트
    for i in range(1, n):
        if Line[i] - ep >= len:  # 다음 말과 엔드포인트의 말 사이의 거리가 주어진 거리보다 크다면? (말을 배치할 수 있다)
            cnt += 1  # 배치한 말의 수 증가
            ep = Line[i]  # 말을 배치한다.
    return cnt


n, c = map(int, input().split())
res = 0
Line = list()
for i in range(n):
    p = int(input())
    Line.append(p)
Line.sort()
lt = 1
rt = Line[n-1]
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= c:  # 배치해야 할 말보다 크거나 같으면 답임.
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
