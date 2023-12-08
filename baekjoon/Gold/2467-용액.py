import heapq

n = int(input())
arr = list(map(int, input().split()))
heap = list()

left = 0
right = n - 1
mini = 2147000000
while left < right:
    v = arr[left] + arr[right]
    # 양 끝이 최소값보다 작다면
    if abs(v) <= mini:
        mini = abs(v)
        heapq.heappush(heap, (mini, arr[left], arr[right]))

    if v <= 0:
        left += 1
    else:
        right -= 1


_, a, b = heapq.heappop(heap)
res = [a, b]
res.sort()
print(*res)
