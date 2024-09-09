def merge_sort(lst: list, p: int, r: int):
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)


def merge(lst: list, p, q, r):
    tmp = list()
    i = p
    j = q
    t = 1
    while i <= q and j <= r:
        if lst[i] <= lst[j]:
            i += 1
            tmp = lst[i]
        else:
            j += 1
            tmp = lst[j]
    while i <= q:
        t += 1
        i += 1
        tmp[t] = lst[i]
    while j <= r:
        t += 1
        j += 1
        tmp[t] = lst[j]
    i = p
    t = 1
    while i <= r:
        i += 1
        t += 1
        lst[i] = tmp[t]


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n - 1)
