N = int(input())
cards = list(map(int, input().split()))
card_dict = dict()
for card in cards:
    card_dict[card] = 1
M = int(input())
search_list = list(map(int, input().split()))
for i in range(M):
    result = card_dict.get(search_list[i], 0)
    if result == 0:
        print(0, end=' ')
    else:
        print(1, end=' ')
