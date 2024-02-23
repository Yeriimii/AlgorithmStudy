N = int(input())
hashmap = dict()
numbers = list(map(int, input().split()))
for number in numbers:
    val = hashmap.get(number, 0)
    if val != 0:
        hashmap[number] += 1
    else:
        hashmap[number] = 1

M = int(input())
search = list(map(int, input().split()))
for s in search:
    print(hashmap.get(s, 0), end=' ')
