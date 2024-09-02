import sys
import heapq

if __name__ == '__main__':
    n = int(input())
    numbers = []
    for _ in range(n):
        heapq.heappush(numbers, int(sys.stdin.readline().rstrip()))

    for _ in range(n):
        print(heapq.heappop(numbers))
