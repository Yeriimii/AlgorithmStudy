'''
ASCII Number
A~Z : 65~90 (26개)
a~z : 97~122 (26개)
'''

a1 = input()
a2 = input()

str1 = [0] * 52
str2 = [0] * 52
for x in a1:
    if x.isupper():
        str1[ord(x)-65] += 1
    if x.islower():
        str1[ord(x)-71] += 1

for x in a2:
    if x.isupper():
        str2[ord(x)-65] += 1
    if x.islower():
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
