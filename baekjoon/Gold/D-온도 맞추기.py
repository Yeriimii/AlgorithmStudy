n = int(input())
init_b = list(map(int, input().split()))
target_b = list(map(int, input().split()))
change_t = list(map(int, input().split()))
even = 0
odd = 0

res = -2147000000
for idx in range(n):
    if abs(target_b[idx] - init_b[idx]) % change_t[idx] != 0:
        res = -1
        break
    else:
        min_cnt = abs(target_b[idx] - init_b[idx]) // change_t[idx]
        if min_cnt % 2 == 0:
            even = 1
            res = max(res, min_cnt)
        elif min_cnt % 2 != 0:
            odd = 1
            res = max(res, min_cnt)

        if even > 0 and odd > 0:
            res = -1
            break

print(res)
