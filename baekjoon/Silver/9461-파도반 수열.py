P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2
for i in range(6, 101):
    P[i] = P[i - 5] + P[i - 1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(P[n])
