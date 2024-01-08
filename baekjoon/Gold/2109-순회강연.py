import heapq

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1]))
p_list = []
for i in lst:
    p = i[0]
    d = i[1]
    heapq.heappush(p_list, p)
    if len(p_list) > d:
        heapq.heappop(p_list)

print(sum(p_list))
