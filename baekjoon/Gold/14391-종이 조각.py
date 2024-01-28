N, M = map(int, input().split())
origin_arr = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
HORIZONTAL = 0
VERTICAL = 1


def piece_calculate(_status_arr: list[list[int]]) -> int:
    total_piece_sum = []
    # 모든 가로 조각 계산
    for row in range(N):
        piece_sum = 0
        for col in range(M):
            # 상태 배열의 상태가 '가로'면 계산
            if _status_arr[row][col] == HORIZONTAL:
                # 기존 가로 조각의 자리수를 한 자리 올리고 원본 배열의 값을 더한다
                piece_sum *= 10
                piece_sum += origin_arr[row][col]
            # 상태 배열의 상태가 '세로'면
            else:
                # 이전까지 계산했던 가로 조각의 값을 전체 조각 합 계산 배열에 추가
                total_piece_sum.append(piece_sum)
                # 다음 가로 조각을 위해 0으로 초기화
                piece_sum = 0
        # 하나의 가로 조각 계산이 끝나면 전체 조각 합 계산 배열에 추가
        total_piece_sum.append(piece_sum)

    # 모든 세로 조각 계산
    for col in range(M):
        piece_sum = 0
        for row in range(N):
            # 상태 배열의 상태가 '세로'면 계산
            if _status_arr[row][col] == VERTICAL:
                # 기존 세로 조각의 자리수를 한 자리 올리고 원본 배열의 값을 더한다
                piece_sum *= 10
                piece_sum += origin_arr[row][col]
            # 상태 배열의 상태가 '가로'면
            else:
                # 이전까지 계산했던 가로 조각의 값을 전체 조각 합 계산 배열에 추가
                total_piece_sum.append(piece_sum)
                # 다음 세로 조각을 위해 0으로 초기화
                piece_sum = 0
        # 하나의 세로 조각 계산이 끝나면 전체 조각 합 계산 배열에 추가
        total_piece_sum.append(piece_sum)
    return sum(total_piece_sum)


def dfs(row: int, col: int, _status_arr: list[list[int]]):
    global answer
    # 재귀 종료 조건
    # N = 2, M = 2 일 때 상태 배열은 4개의 값을 가짐
    # L = 4 이면 상태 배열의 모든 값이 '가로' 또는 '세로' 상태를 가짐
    # 상태 배열의 모든 값이 상태를 갖게 되었을 때 원본 배열을 계산
    if row >= N:
        answer = max(answer, piece_calculate(_status_arr))
    elif col >= M:
        dfs(row + 1, 0, _status_arr)
    else:
        # (i, j) 위치를 '가로' 상태로 두고 재귀 호출
        _status_arr[row][col] = HORIZONTAL
        dfs(row, col + 1, _status_arr)

        # (i, j) 위치를 '세로' 상태로 두고 재귀 호출
        _status_arr[row][col] = VERTICAL
        dfs(row, col + 1, _status_arr)


status_arr = [[0 for _ in range(M)] for _ in range(N)]
dfs(0, 0, status_arr)
print(answer)
