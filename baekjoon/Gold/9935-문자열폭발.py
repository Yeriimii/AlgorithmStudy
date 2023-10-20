from collections import deque

if __name__ == '__main__':
    string = ' '.join(input()).split()
    bomb = ' '.join(input()).split()
    deleted = deque()
    res = deque()
    Q = deque(string)
    last = len(bomb) - 1
    while Q:
        w = Q.popleft()
        if w == bomb[last]:
            cnt = 0
            res.append(w)
            if len(res) >= len(bomb):
                for i in range(len(bomb) - 1, -1, -1):
                    ww = res.pop()
                    if bomb[i] == ww:
                        deleted.append(ww)
                        cnt += 1
                    else:
                        res.append(ww)
                        for _ in range(cnt):
                            res.append(deleted.pop())
                        break
        else:
            res.append(w)
    if res:
        while res:
            print(res.popleft(), end='')
        print()
    else:
        print('FRULA')
