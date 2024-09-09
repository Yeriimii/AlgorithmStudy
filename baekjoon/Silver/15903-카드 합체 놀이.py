import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    heapq.heapify(cards)
    for _ in range(m):
        a1 = heapq.heappop(cards)
        a2 = heapq.heappop(cards)
        heapq.heappush(cards, a1 + a2)
        heapq.heappush(cards, a1 + a2)

    print(sum(cards))
