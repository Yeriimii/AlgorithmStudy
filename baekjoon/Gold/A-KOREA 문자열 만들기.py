def find_word(word: str, idx: int):
    global res

    if idx >= len(arr):
        return -1

    if arr[idx] == word:
        res += 1
        return idx + 1
    else:
        return find_word(word, idx + 1)


arr = input()
res = 0
next_idx = 0
word_list = ['K', 'O', 'R', 'E', 'A']
keep_going = True
while keep_going:
    for w in word_list:
        next_idx = find_word(w, next_idx)
        if next_idx == -1:
            keep_going = False
            break

print(res)
