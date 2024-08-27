from collections import deque


def sum_weight(queue: deque):
    total = 0
    for _weight, _ in queue:
        total += _weight
    return total


if __name__ == '__main__':
    n, w, L = map(int, input().split())
    trucks = deque()
    truck_weights = list(map(int, input().split()))
    bridges = [0 for _ in range(w)]
    for weight in truck_weights:
        trucks.append((weight, 0))

    total_time = 0
    q = deque()
    while q or trucks:
        i = len(q)
        while i > 0:
            weight, position = q.popleft()
            if position < w:
                q.append((weight, position + 1))
            i -= 1

        if trucks:
            weight, position = trucks.popleft()
            if weight + sum_weight(q) <= L and len(q) < w:
                q.append((weight, position + 1))
            else:
                trucks.appendleft((weight, position))

        total_time += 1

    print(total_time)
