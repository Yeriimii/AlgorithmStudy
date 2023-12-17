INF = 2147000000
n = int(input())
rgb = []
ans = INF
for _ in range(n):
    rgb.append(list(map(int, input().split())))


for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    # 첫 번째 집의 색을 R, G, B 각각의 경우로 칠했을 때
    dp[0][i] = rgb[0][i]
    # 두 번째 집부터 비용 계산
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    # 첫 번째가 R이면 마지막 집이 R이 아닐 때 최소값
    # 첫 번째가 G면 마지막 집이 G가 아닐 때 최소값
    # 첫 번째가 B면 마지막 집이 B가 아닐 때 최소값
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)