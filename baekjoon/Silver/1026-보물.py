import heapq

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_heapA = []
max_heapB = []

for i in range(N):
    heapq.heappush(min_heapA, A[i])
    heapq.heappush(max_heapB, -B[i])

res = 0
for i in range(N):
    a = heapq.heappop(min_heapA)
    b = -heapq.heappop(max_heapB)
    res += a * b
print(res)
