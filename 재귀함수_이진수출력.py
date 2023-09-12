import sys


def DFS(x):
    if x == 0:
        return
    DFS(x // 2)
    print(x % 2, end='')


if __name__ == "__main__":
    DFS(11)  # 1011
