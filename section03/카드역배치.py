card = list(range(0, 21))
for _ in range(10):
    ai, bi = map(int, input().split())
    for i in range((bi-ai+1)//2):
        card[ai+i], card[bi-i] = card[bi-i], card[ai+i]
    # card[ai:bi+1] = reversed(card[ai:bi+1])
card.pop(0)
for x in card:
    print(x, end=' ')
