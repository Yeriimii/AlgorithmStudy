import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
numbers = list(map(int, ' '.join(input().rstrip()).split()))

res = list()
for number in numbers:
    while res and K > 0:
        if res[-1] < number:
            res.pop()
            K -= 1
        else:
            break
    res.append(number)

if K > 0:
    for i in range(K):
        res.pop()

for x in res:
    print(x, end='')
