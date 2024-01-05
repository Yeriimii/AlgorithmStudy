def dfs(L, end, include_index, excepted_idexes):
    global three_min_val, two_min_val
    if L == end:
        if end == 3:
            three_min_val = min(three_min_val, sum(three))
        elif end == 2:
            two_min_val = min(two_min_val, sum(two))
        return
    else:
        for i in range(6):
            if i != include_index and i not in excepted_idexes:
                if end == 3:
                    three[L] = numbers[i]
                elif end == 2:
                    two[L] = numbers[i]
                excepted_idexes.append(i)
                excepted_idexes.append(5 - i)
                dfs(L + 1, end, include_index, excepted_idexes)
                excepted_idexes.pop()
                excepted_idexes.pop()


N = int(input())
numbers = list(map(int, input().split()))
three = [0] * 3
two = [0] * 2
three_min_val = 2147000000
two_min_val = 2147000000
one_min_val = min(numbers)
for i in range(6):
    three[0] = numbers[i]
    dfs(1, 3, i, [5 - i])
    two[0] = numbers[i]
    dfs(1, 2, i, [5 - i])
if N > 1:
    n_floor = three_min_val * 4 + two_min_val * 4 * (N - 2) + one_min_val * ((N - 2) ** 2)
    others = (two_min_val * 4 + one_min_val * 4 * (N - 2)) * (N - 1)
    res = n_floor + others
else:
    res = sum(numbers) - max(numbers)
print(res)
