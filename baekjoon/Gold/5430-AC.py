import sys
from collections import deque

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        cmd_Q = deque(sys.stdin.readline())
        n = int(sys.stdin.readline())
        if n != 0:
            num_Q = deque(list(map(int, sys.stdin.readline().replace('\n', '').replace('[', '').replace(']', '').split(','))))
        else:
            num_Q = sys.stdin.readline()
            num_Q = list()
        cnt = 0
        while cmd_Q:
            cur = cmd_Q.popleft()
            if cur == 'R':
                cnt += 1
            elif cur == 'D':
                if len(num_Q) == 0:
                    num_Q.clear()
                    num_Q.append('error')
                    break
                else:
                    if cnt % 2 == 0:
                        num_Q.popleft()
                    elif cnt % 2 == 1:
                        num_Q.pop()
        if 'error' not in num_Q:
            if cnt % 2 == 0:
                print('[' + ','.join(map(str, num_Q)) + ']')
            else:
                num_Q.reverse()
                print('[' + ','.join(map(str, num_Q)) + ']')
        else:
            print('error')
