if __name__ == '__main__':
    target = input()
    n = int(input())
    answer = 0
    for _ in range(n):
        ring = input()
        if target in ring * 2:
            answer += 1
    print(answer)
