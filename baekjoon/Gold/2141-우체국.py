"""
L1 공간에서 sum(|xi - a| * b)의 최소값은 표본의 중앙값이 위치한 값임을 이용한 문제
"""
import sys

input = sys.stdin.readline

N = int(input())
villages = []
total_population = 0
for _ in range(N):
    n_village, n_population = map(int, input().split())
    villages.append([n_village, n_population])
    total_population += n_population

villages.sort(key=lambda x: x[0])

res = 0
for i in range(N):
    res += villages[i][1]
    if res >= total_population / 2:
        print(villages[i][0])
        break
