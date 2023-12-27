N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = N - 1

min_v = abs(solutions[left] + solutions[right])
res = (solutions[left], solutions[right])

while left < right:
    solutions_sum = solutions[left] + solutions[right]

    if abs(solutions_sum) < min_v:
        min_v = abs(solutions_sum)
        res = (solutions[left], solutions[right])
        if min_v == 0:
            break

    if solutions_sum < 0:
        left += 1
    else:
        right -= 1

print(*res)
