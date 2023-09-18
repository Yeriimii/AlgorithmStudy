n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for j in range(n-1):
    use_word = input()
    p[use_word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
