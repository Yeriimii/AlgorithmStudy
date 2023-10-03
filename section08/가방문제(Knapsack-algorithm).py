if __name__ == '__main__':
    n, m = map(int, input().split())
    dy = [0] * (m+1)
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            # 현재 보석을 가방에 최대한 담음을 가정했을 때
            dy[j] = max(dy[j], dy[j-w] + v)
    print(dy[m])
