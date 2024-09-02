if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        answer = 0
        numbers.sort()

        for i in range(2, n):
            answer = max(answer, abs(numbers[i] - numbers[i - 2]))
        print(answer)
