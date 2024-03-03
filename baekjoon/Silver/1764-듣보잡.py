import sys

input = sys.stdin.readline
N, M = map(int, input().split())
no_hear = dict()
no_seen = dict()
no_hear_seen = []
for _ in range(N):
    no_hear[input()] = 1
for _ in range(M):
    person = input()
    check = no_hear.get(person, 0)
    if check == 1:
        no_hear_seen.append(person)
print(len(no_hear_seen))
for person in sorted(no_hear_seen):
    print(person)
