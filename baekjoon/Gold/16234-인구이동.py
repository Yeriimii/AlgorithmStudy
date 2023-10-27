import sys

sys.setrecursionlimit(10**6)


def dfs(x, y):
    global union_list, total_population
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < N and (not visited[xx][yy]):
            if L <= abs(board[x][y]-board[xx][yy]) <= R:
                visited[xx][yy] = True
                union_list.append((xx, yy))
                total_population += board[xx][yy]
                dfs(xx, yy)


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    day = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    # 국가 탐색하며 연합 찾기
                    visited[i][j] = True
                    union_list = list()
                    union_list.append((i, j))
                    total_population = board[i][j]
                    dfs(i, j)
                    # 수정된 국가별 인구
                    modified_population = int(total_population / len(union_list))
                    # 연합에 한 국가만 있으면 연합결성 X
                    if len(union_list) != 1:
                        for k, l in union_list:
                            board[k][l] = modified_population
                    else:  # 연합결성이 되지 않으면 카운팅
                        cnt += 1
        # 카운팅 된 숫자가 2차원 배열의 개수라는 뜻은 연합이 된 적이 없다는 뜻 -> 인구이동 종료
        if cnt == N**2:
            print(day)
            break
        else:
            day += 1
