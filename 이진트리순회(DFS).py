import sys


def DFS(v):
    if v > 7:
        return
    else:
        # # 전위순회
        # print(v, end=' ')  # 부모 노드 출력
        # DFS(v * 2)  # 왼쪽: 부모 노드 * 2
        # DFS(v * 2 + 1)  # 오른쪽: 부모 노드 * 2 + 1
        #
        # # 중위순회
        # DFS(v * 2)  # 왼쪽: 부모 노드 * 2
        # print(v, end=' ')  # 부모 노드 출력
        # DFS(v * 2 + 1)  # 오른쪽: 부모 노드 * 2 + 1

        # 후위순회
        DFS(v * 2)  # 왼쪽: 부모 노드 * 2
        DFS(v * 2 + 1)  # 오른쪽: 부모 노드 * 2 + 1
        print(v, end=' ')  # 부모 노드 출력


if __name__ == "__main__":
    DFS(1)
