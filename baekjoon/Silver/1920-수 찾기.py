N = int(input())
numbers = list(map(int, input().split()))
hashmap = dict()
for i in range(N):
    hashmap[numbers[i]] = 1

M = int(input())
search = list(map(int, input().split()))
for j in range(M):
    if hashmap.get(search[j], 0) == 1:
        print(1)
    else:
        print(0)
