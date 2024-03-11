N = int(input())
road_lengths = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))

min_cost = 0
L = 0
R = 0
while R < N - 1:
    if R == 0:
        min_cost += oil_cost[L] * road_lengths[R]
    else:
        if oil_cost[L] > oil_cost[R]:
            L = R
        min_cost += oil_cost[L] * road_lengths[R]
    R += 1
print(min_cost)
