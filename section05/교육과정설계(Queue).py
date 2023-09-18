from collections import deque

need = input()
n = int(input())
res = list()
for i in range(n):
    copy_need = deque(need)
    plan = deque(input())
    for char in plan:
        if char in copy_need:
            if char != copy_need.popleft():
                res.append(f"#{(i + 1)} NO")
                break
    else:
        if len(copy_need) == 0:
            res.append(f"#{(i + 1)} YES")
        else:
            res.append(f"#{(i + 1)} NO")

for _ in res:
    print(_)
