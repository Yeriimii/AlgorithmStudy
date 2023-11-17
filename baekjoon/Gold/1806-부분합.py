if __name__ == '__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_sum = 0
    left = 0
    right = 0
    res = 2147000000
    while True:
        if arr_sum >= s:
            res = min(res, right - left)
            arr_sum -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            arr_sum += arr[right]
            right += 1
    if res == 2147000000:
        print(0)
    else:
        print(res)
