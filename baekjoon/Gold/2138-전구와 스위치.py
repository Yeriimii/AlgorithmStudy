n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    copied_A = A[:]
    press = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 pass
        if copied_A[i - 1] == B[i - 1]:
            continue
        # 상태가 다를 경0우
        press += 1
        for j in range(i - 1, i + 2):
            if j < n:
                # 반전
                copied_A[j] = 1 - copied_A[j]

    if copied_A == B:
        return press
    else:
        return 1e9


# 첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
if res != 1e9:
    print(res)
else:
    print(-1)
