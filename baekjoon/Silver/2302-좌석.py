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
