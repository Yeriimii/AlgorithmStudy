N = int(input())
numbers = list(map(int, input().split()))
NGE = [-1] * N
stack = [0]

for i in range(1, N):
    # numbers[i]의 오른쪽에 있으면서 numbers[i]보다 큰 수중 가장 왼쪽의 값
    while stack and numbers[stack[-1]] < numbers[i]:
        NGE[stack.pop()] = numbers[i]
    stack.append(i)

print(*NGE)
