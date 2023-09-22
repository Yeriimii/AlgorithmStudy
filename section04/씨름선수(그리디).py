n = int(input())
body: list[tuple[int, ...]] = [tuple(map(int, input().split())) for _ in range(n)]
body.sort(reverse=True, key=lambda x : (x[0], x[1]))  # 키 기준 정렬
cnt = 0
largest = 0
for h, w in body:  # 첫 번째는 키로 전부 다 이기기 때문에 카운팅
    if w > largest:
        largest = w
        cnt += 1
print(cnt)
