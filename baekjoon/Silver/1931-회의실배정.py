n = int(input())
List = [tuple(map(int, input().split())) for _ in range(n)]
List.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for s, e in List:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)

