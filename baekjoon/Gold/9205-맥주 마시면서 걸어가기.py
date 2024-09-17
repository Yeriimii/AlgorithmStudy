from collections import deque


def check(target_x: int, target_y: int, current_beer: int):
    global answer
    if abs(target_x - start_x) + abs(target_y - start_y) <= 1000 and 0 <= current_beer <= 20:
        answer = True
        return True
    answer = False
    return False


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = False
        start_x, start_y = map(int, input().split())
        conveniences = [list(map(int, input().split())) for _ in range(n)]
        conveniences.sort()
        end_x, end_y = map(int, input().split())

        q = deque()
        q.append((end_x, end_y, 20))
        visited = [False for _ in range(n)]
        while q:
            tx, ty, beer = q.popleft()
            if check(tx, ty, beer):
                break
            for i in range(n):
                dist = abs(conveniences[i][0] - tx) + abs(conveniences[i][1] - ty)
                if dist > 1000:
                    continue
                if dist % 50 > 0:
                    beer -= 1
                beer -= dist // 50
                beer += 20 - beer
                if not visited[i]:
                    visited[i] = True
                    q.append((conveniences[i][0], conveniences[i][1], beer))

        if answer:
            print("happy")
        else:
            print("sad")
