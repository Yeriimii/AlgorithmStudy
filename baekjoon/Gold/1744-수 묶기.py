n = int(input())
minus = list()
plus = list()
zero = list()
for _ in range(n):
    v = int(input())
    if v == 0:
        zero.append(v)
    elif v > 0:
        plus.append(v)
    else:
        minus.append(v)

plus.sort()
minus.sort(reverse=True)
tmp = list()
res = 0
while plus:
    tmp.append(plus.pop())
    if len(tmp) == 2:
        a = tmp.pop()
        b = tmp.pop()
        if a == 1 or b == 1:
            res += a + b
        else:
            res += a * b

if len(tmp) == 1:
    res += tmp.pop()

while minus:
    tmp.append(minus.pop())
    if len(tmp) == 2:
        res += tmp.pop() * tmp.pop()

if len(tmp) == 1:
    if len(zero) == 0:
        res += tmp.pop()

print(res)
