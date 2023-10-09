def DFS(r):
    if r > n:
        return
    else:
        print(tree[r][0], end='')
        for i in range(r+1, n):
            if tree[i][0] == tree[r][1]:
                DFS(i)
                break
        for i in range(r+1, n):
            if tree[i][0] == tree[r][2]:
                DFS(i)
                break


def inorder(r):
    if r > n:
        return
    else:
        for i in range(r+1, n):
            if tree[i][0] == tree[r][1]:
                inorder(i)
                break
        if tree[r][0] != '.':
            print(tree[r][0], end='')
        for i in range(r+1, n):
            if tree[i][0] == tree[r][2]:
                inorder(i)
                break


def postorder(r):
    if r > n:
        return
    else:
        for i in range(r + 1, n):
            if tree[i][0] == tree[r][1]:
                postorder(i)
                break
        for i in range(r + 1, n):
            if tree[i][0] == tree[r][2]:
                postorder(i)
                break
        if tree[r][0] != '.':
            print(tree[r][0], end='')


if __name__ == '__main__':
    n = int(input())
    tree = [input().split() for _ in range(n)]
    DFS(0)
    print()
    inorder(0)
    print()
    postorder(0)
