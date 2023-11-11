def find_late_element(idx):
    result = 0
    max_idx = -2147000000

    for x in multi_tab:
        try:
            x_idx = seq[idx:].index(x)
        except:
            x_idx = k
        if max_idx < x_idx:
            result, max_idx = x, x_idx

    return result


if __name__ == '__main__':
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    multi_tab = set()
    cnt = 0

    for idx, num in enumerate(seq):
        multi_tab.add(num)
        if len(multi_tab) > n:
            cnt += 1
            late_used = find_late_element(idx)
            multi_tab.discard(late_used)

    print(cnt)
