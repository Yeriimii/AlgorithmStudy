n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
# 시작점부터 가장자리 채우기 (당연한 최단거리)
dy[0][0] = arr[0][0]
for i in range(n):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0]

# dy table 채우기
for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-i])  # 위에서 오는 최소비용과 왼쪽에서 오는 최소비용 중 작은 값
print(dy[n-1][n-1])
