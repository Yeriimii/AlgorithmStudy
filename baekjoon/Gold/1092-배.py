N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0

if boxes[0] > cranes[0]:
    cnt = -1
else:
    while boxes:
        for i in range(len(cranes)):
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    boxes.pop(j)
                    break
        cnt += 1

print(cnt)
