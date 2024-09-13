if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort()

    # dp[i] : i원을 만들 수 있는 모든 경우의 수
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1  # dp[0]: 0원을 만들 수 있는 경우의 수 = 1 (아무 것도 사용하지 않음)

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]  # dp[4] = dp[4] + dp[2]

    print(dp[k])
