import sys


def DFS(v):
    if v == (n+1):  # 단말 노드 -> 출력
        for i in range(1, n+1):
            if check[i] == 1:  # 사용하는 원소만 출력
                print(i, end=' ')
        print()
    else:
        check[v] = 1  # 사용한다
        DFS(v+1)
        check[v] = 0  # 사용 안한다
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n+1)  # 사용여부 체크
    DFS(1)
