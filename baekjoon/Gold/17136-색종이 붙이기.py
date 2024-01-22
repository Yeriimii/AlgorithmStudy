import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
paper = [list(map(int, input().split())) for _ in range(10)]
remain = [5 for _ in range(5)]
total = 25


def check(y, x, offset):
    for i in range(y, y + offset + 1):
        for j in range(x, x + offset + 1):
            if paper[i][j] != 1:
                return False
    return True


def backtracking(r, c, cnt):
    global remain, total
    if r >= 10:
        total = min(total, cnt)
        return
    if c >= 10:
        backtracking(r + 1, 0, cnt)
        return
    if paper[r][c] == 1:
        for k in range(5):
            if remain[k] == 0:
                continue
            if r + k >= 10 or c + k >= 10:
                continue
            if not check(r, c, k):
                break
            for i in range(r, r + k + 1):
                for j in range(c, c + k + 1):
                    paper[i][j] = 0
            remain[k] -= 1
            backtracking(r, c + k + 1, cnt + 1)
            remain[k] += 1
            for i in range(r, r + k + 1):
                for j in range(c, c + k + 1):
                    paper[i][j] = 1
    else:
        backtracking(r, c + 1, cnt)


backtracking(0, 0, 0)
print(-1 if total == 25 else total)
