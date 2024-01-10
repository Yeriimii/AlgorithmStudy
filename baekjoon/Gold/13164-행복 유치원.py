N, K = map(int, input().split())
heights = list(map(int, input().split()))
sub = []
for i in range(1, N):
    subtract = heights[i] - heights[i - 1]
    sub.append(subtract)

sub.sort()

for _ in range(K - 1):
    sub.pop()

print(sum(sub))
