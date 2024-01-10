import sys
import heapq

input = sys.stdin.readline

N = int(input())
quiz = []
Q = []
for _ in range(N):
    deadline, cup_noodle = map(int, input().rstrip().split())
    quiz.append([deadline, cup_noodle])

quiz.sort(key=lambda x: x[0])

for i in range(N):
    deadline, cup_noodle = quiz[i]
    heapq.heappush(Q, cup_noodle)
    if len(Q) > deadline:
        heapq.heappop(Q)

print(sum(Q))
