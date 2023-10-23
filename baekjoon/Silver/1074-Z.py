def DFS(L, size, r, c, num):
    if size == 2:
        if r == 0 and c == 0:
            num += 0
        elif r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
        print(int(num))
    else:
        if r >= size // 2 and c >= size // 2:
            # 아래 오른쪽 (4 사분면)
            num += (2 ** (N - L)) ** 2 * 3
            DFS(L+1, size//2, r - size//2, c - size//2, num)
        elif r >= size // 2 and c < size // 2:
            # 아래 왼쪽 (3 사분면)
            num += (2 ** (N - L)) ** 2 * 2
            DFS(L+1, size//2, r - size//2, c, num)
        elif r < size // 2 and c >= size // 2:
            # 위 오른쪽 (1 사분면)
            num += (2 ** (N - L)) ** 2 * 1
            DFS(L+1, size//2, r, c - size//2, num)
        else:
            # 위 왼쪽 (1 사분면)
            num += (2 ** (N - L)) ** 2 * 0
            DFS(L+1, size//2, r, c, num)


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    DFS(1, 2**N, r, c, 0)
