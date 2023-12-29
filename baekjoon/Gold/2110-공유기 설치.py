import sys

input = sys.stdin.readline

N, C = map(int, input().split())
home_list = list()

for _ in range(N):
    home_list.append(int(input().rstrip()))
home_list.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        cnt = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                cnt += 1
                current = array[i]

        if cnt >= C:
            global res
            res = mid
            start = mid + 1
        else:
            end = mid - 1


start = 1
end = home_list[N-1] - home_list[0]
res = 0

binary_search(home_list, start, end)
print(res)
