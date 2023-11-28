n = int(input())
weights = list(map(int, input().split()))
acc = [0] * 2

weights.sort()

for i in range(n):
    new_acc_start = acc[0] + weights[i]
    new_acc_end = acc[1] + weights[i]

    if new_acc_start <= acc[1] + 1:
        acc[1] = new_acc_end
    else:
        break
print(acc[1] + 1)
