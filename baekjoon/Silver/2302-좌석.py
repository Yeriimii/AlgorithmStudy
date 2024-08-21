n = int(input())
m = int(input())
reserved = [False for _ in range(n + 1)]
for _ in range(m):
    reserved[int(input())] = True

dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    if reserved[i] or reserved[i - 1]:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp[-1])

# n 번째에 해당하는 입장권이 n-1 번쨰와 바꾸냐 안바꾸냐에 따라 값이 달라진다.
# 기본 점화식: dp[i] = dp[i - 1] + dp[i - 2]
# VIP 좌석인 경우: 고정되있는 자리일 수 밖에 없기 때문에 i 번째와 i - 1 번쨰를 바꾸지 못한다.
# => dp[i] = dp[i - 1] 값과 동일
