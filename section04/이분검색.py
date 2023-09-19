n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0  # point var
rt = n-1  # point var
while lt <= rt:
    mid = (lt + rt) // 2  # point var
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
