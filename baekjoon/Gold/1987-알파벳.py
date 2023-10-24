import sys
from collections import deque

# deque가 아닌 set을 활용 : 문자열, 재방문해야하는 문제 때문에 현재 깊이를 저장해야 함
# https://leeingyun96.tistory.com/22

if __name__ == "__main__":
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    r, c = map(int, input().split())
    board = [' '.join(sys.stdin.readline()).split() for _ in range(r)]
    # Q = deque()
    # Q.append((0, 0, board[0][0]))
    Q = set()
    Q.add((0, 0, board[0][0]))
    max_len = -2147000000
    while Q:
        curr = Q.pop()
        if max_len < len(curr[2]):
            max_len = len(curr[2])

        if max_len == 26:
            break

        for i in range(4):
            xx = curr[0] + dx[i]
            yy = curr[1] + dy[i]
            curr_str = curr[2]
            if 0 <= xx < r and 0 <= yy < c and board[xx][yy] not in curr_str:
                Q.add((xx, yy, curr_str + board[xx][yy]))
    print(max_len)
