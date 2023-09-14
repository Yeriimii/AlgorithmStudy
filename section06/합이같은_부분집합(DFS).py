import sys


def DFS(L, sum):  # L: Level(트리 레벨)
    if sum > total // 2:  # 시간복잡도 개선
        return

    if L == n:  # leaf node
        if sum == (total - sum):
            print("YES")
            sys.exit(0)  # program terminate
    else:
        DFS(L+1, sum + num_lst[L])  # root node 포함
        DFS(L+1, sum)  # root node 미포함


if __name__ == "__main__":
    n = int(input())  # 원소 개수
    num_lst = list(map(int, input().split()))
    total = sum(num_lst)
    DFS(0, 0)
    print("NO")
