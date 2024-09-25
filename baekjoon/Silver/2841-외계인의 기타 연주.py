import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, p = map(int, input().strip().split())
    g = [[] for _ in range(7)]
    answer = 0
    for _ in range(n):
        l, p = map(int, input().strip().split())
        if len(g[l]) == 0 or g[l][-1] < p:
            answer += 1
            g[l].append(p)
        elif g[l][-1] == p:
            continue
        else:
            while True:
                g[l].pop()
                answer += 1
                if len(g[l]) == 0 or g[l][-1] < p:
                    answer += 1
                    g[l].append(p)
                    break
                elif g[l][-1] == p:
                    break
    print(answer)
