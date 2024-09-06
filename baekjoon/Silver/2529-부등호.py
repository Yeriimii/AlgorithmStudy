def check(left: int, right: int, operation: str):
    if operation == '<':
        if left < right:
            return True
    elif operation == '>':
        if left > right:
            return True
    return False


def dfs(level: int, number: str):
    if level == k + 1:
        answer.append(number)
        return
    else:
        for i in range(10):
            if visited[i]:
                continue
            if level == 0 or check(int(number[level - 1]), i, signs[level - 1]):
                visited[i] = True
                dfs(level + 1, number + str(i))
                visited[i] = False


if __name__ == '__main__':
    k = int(input())
    signs = input().split()
    visited = [False for _ in range(10)]
    answer = []
    dfs(0, '')
    answer.sort()
    print(answer[-1])
    print(answer[0])
