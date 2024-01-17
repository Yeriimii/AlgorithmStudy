N = int(input())
cnt = 9
arr = []


def dfs(L):
    """
    :param L: 자리수
    :return:
    """
    global cnt, end_condition
    if L == end_condition - 1:
        cnt += 1
        if cnt == N:
            for x in arr:
                print(x, end='')
            exit(0)
    else:
        for i in range(0, 10):
            if arr[L] > i:
                arr.append(i)
                dfs(L + 1)
                arr.pop()
            else:
                break


if N == 0:
    print(0)
elif N < 10:
    print(N)
else:
    for end_condition in range(2, 12):
        for i in range(1, 10):
            arr.append(i)
            dfs(0)
            arr.pop()
    print(-1)
