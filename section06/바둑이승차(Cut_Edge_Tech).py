import sys


def DFS(L, sum):
    global max_w

    if sum > c:
        return

    if L == n:
        if max_w < sum:
            max_w = sum
        return

    if max_w < sum:
        max_w = sum

    DFS(L+1, sum + dogs[L])
    DFS(L+1, sum)

if __name__ == "__main__":
    c, n = map(int, input().split())
    dogs = [0] * n
    max_w = 0

    for i in range(n):
        dogs[i] = int(input())

    DFS(0, 0)
    print(max_w)

def DFS_해설(L, sum, total_sum):
    global result

    if sum + (total - total_sum) < result:  # 지금까지 판단한 바둑이들의 무게와 앞으로 판단할 바둑이들의 무게의 합이 result보다 적으면 의미 X -> cut
        return

    if sum > c:  # cut
        return

    if L == n:
        if result < sum:
            result = sum
    else:
        DFS_해설(L+1, sum + dogs[L], total_sum + dogs[L])
        DFS_해설(L+1, sum, total_sum + dogs[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    dogs = [0] * n
    result = -2147000000
    total = sum(dogs)
    for i in range(n):
        dogs[i] = int(input())

    DFS_해설(0, 0, 0)
    print(result)
