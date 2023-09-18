from collections import defaultdict

str1 = dict()
str2 = dict()
a1 = input()
a2 = input()
for i in a1:
    str1[i] = str1.get(i, 0) + 1
for i in a2:
    str2[i] = str2.get(i, 0) + 1

for k in str1.keys():
    if k in str2.keys():
        if str1[k] != str2[k]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
