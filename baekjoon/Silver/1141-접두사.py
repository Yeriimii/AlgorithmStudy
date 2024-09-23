if __name__ == '__main__':
    n = int(input())
    words = list()
    for _ in range(n):
        words.append(input())
    words.sort(key=lambda x: len(x), reverse=True)

    answer = 0
    for i in range(n):
        is_prefix = False
        for j in range(i):
            if words[j].startswith(words[i]):
                is_prefix = True
                break
        if not is_prefix:
            answer += 1

    print(answer)
