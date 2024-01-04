import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

res = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learned_char = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learned_char[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global res

    if cnt == k - 5:
        readable_cnt = 0
        for word in words:
            is_readable = True
            for w in word:
                if not learned_char[ord(w) - ord('a')]:
                    is_readable = False
                    break
            if is_readable:
                readable_cnt += 1
        res = max(res, readable_cnt)
        return

    for i in range(idx, 26):
        if not learned_char[i]:
            learned_char[i] = True
            dfs(i, cnt + 1)
            learned_char[i] = False


dfs(0, 0)
print(res)
