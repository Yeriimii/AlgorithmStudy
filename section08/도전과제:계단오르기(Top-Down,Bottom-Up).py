'''
Top-Down: memoization
'''
def DFS(s):
    if dy[s] > 0:
        return dy[s]

    if s == 1 or s == 2:
        return s
    else:
        dy[s] = DFS(s-1) + DFS(s-2)
        return dy[s]


if __name__ == '__main__':
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))


'''
Bottom-Up: Dynamic Programming
'''
n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]
print(dy[n])
