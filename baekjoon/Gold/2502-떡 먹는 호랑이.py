if __name__ == '__main__':
    D, K = map(int, input().split())
    dp = [0 for _ in range(D + 1)]
    dp[1] = 1
    dp[2] = 1

    while True:
        for i in range(3, D + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            if dp[D] == K:
                print(dp[1])
                print(dp[2])
                break
            elif dp[D] > K:
                dp[1] += 1
                dp[2] = dp[1]
            else:
                dp[2] += 1
