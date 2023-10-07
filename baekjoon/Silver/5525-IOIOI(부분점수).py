n = int(input())
M = int(input())
S = input()
P = 'I' + 'OI' * n
cnt = 0
start = 0
while True:
    pos = S.find(P, start)
    if pos != -1:
        next_I = S.find('I', pos + 1)
        next_O = S.find('O', pos + 1)

        if next_I == -1 or next_O == -1:
            break

        if next_O > next_I:
            start = next_O
        else:
            start = next_I

        cnt += 1
    else:
        break
print(cnt)

'''KMP 알고리즘'''
def compute_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        pi[i] = j

    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_pi(pattern)
    cnt = 0
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            cnt += 1
            j = pi[j - 1]

    return cnt

n = int(input())
M = int(input())
S = input()
P = 'I' + 'OI' * n

result = kmp_search(S, P)
print(result)
