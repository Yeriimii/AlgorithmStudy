if __name__ == '__main__':
    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    sum_visitors = sum(visitors[:X])
    interval_value = sum_visitors
    cnt = 1
    if sum_visitors == 0:
        print("SAD")
    else:
        for i in range(X, N):
            interval_value -= visitors[i - X]
            interval_value += visitors[i]
            if interval_value > sum_visitors:
                sum_visitors = interval_value
                cnt = 1
            elif interval_value == sum_visitors:
                cnt += 1

        print(sum_visitors)
        print(cnt)
