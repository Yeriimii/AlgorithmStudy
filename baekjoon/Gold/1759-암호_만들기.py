def dfs(L, s):
    if L == l:
        consonant_cnt, vowel_cnt = 0, 0
        for i in range(l):
            if res[i] in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            for k in range(L):
                print(res[k], end='')
            print()
    else:
        for i in range(s, c):
            res[L] = char_list[i]
            dfs(L + 1, i + 1)


if __name__ == '__main__':
    vowel = ['a', 'e', 'i', 'o', 'u']
    l, c = map(int, input().split())
    char_list = input().split()
    char_list.sort()
    res = [0] * (l + 1)
    dfs(0, 0)
