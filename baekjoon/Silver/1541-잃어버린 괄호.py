s = input()
minus_cnt = s.count('-')
s_split = s.split('-')
plus = []
minus = []
i = 1
while minus_cnt > 0:
    x = s_split[i]
    y = x.split('+')
    tmp = 0
    for z in y:
        tmp += int(z)
    minus.append(tmp)
    s_split.pop(i)
    minus_cnt -= 1

for x in s_split:
    y = x.split('+')
    tmp = 0
    for z in y:
        if z == '':
            continue
        tmp += int(z)
    plus.append(tmp)

res = sum(plus) - sum(minus)
print(res)
