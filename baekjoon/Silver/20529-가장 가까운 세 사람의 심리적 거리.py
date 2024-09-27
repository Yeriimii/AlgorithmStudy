def dfs(l: int, s: int, q: list):
    global answer

    if l == 3:
        score = 0
        for i in range(4):
            if q[0][i] != q[1][i]:
                score += 1
            if q[0][i] != q[2][i]:
                score += 1
            if q[1][i] != q[2][i]:
                score += 1
        answer = min(answer, score)
    else:
        for i in range(s, n):
            q.append(mbti_list[i])
            dfs(l + 1, i + 1, q)
            q.pop()


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mbti_list = input().split()
        if n > 33:
            print(0)
        else:
            answer = 2e9
            dfs(0, 0, [])
            print(answer)
