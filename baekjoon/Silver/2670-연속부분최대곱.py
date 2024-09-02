if __name__ == '__main__':
    n = int(input())
    numbers = [float(input()) for _ in range(n)]

    for i in range(1, n):
        numbers[i] = max(numbers[i], numbers[i - 1] * numbers[i])

    print(f'{max(numbers):.3f}')
