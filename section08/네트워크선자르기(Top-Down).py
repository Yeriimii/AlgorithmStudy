def DFS(len):
    if dy[len] > 0:  # dy에 값이 있다면 바로 리턴 (cut)
        return dy[len]

    if len == 1 or len == 2:  # memoization
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__ == '__main__':
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))
    print(dy)
