N = int(input())
today = 0
hw = []
for _ in range(N):
    d, w = map(int, input().split())
    hw.append([d, w])
hw.sort(key=lambda x: (x[1], x[0]), reverse=True)
assigned = [False] * 1001

res = 0
for day, score in hw:
    for i in range(day, 0, -1):
        if assigned[i]:
            continue

        assigned[i] = True
        res += score
        break
print(res)
