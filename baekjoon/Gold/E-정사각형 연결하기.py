# T = int(input())
# dy = [0] * 1000000001
# dy[1] = 4
#
# for i in range(T):
#     case = int(input())
#     if dy[case] > 0:
#         print(dy[case])
#     else:
#         index = -1
#         for j in range(2, 1000000001):
#             if j % 2 == 0:
#                 index += 2
#             else:
#                 index += 1
#             dy[j] = dy[1] * j - 2 * index
#             if j == case:
#                 break
#         print(dy[case])

T = int(input())
dy = {1: 4}  # 딕셔너리를 사용하여 필요한 부분만 메모이제이션

def calculate_values(up_to):
    if up_to <= len(dy):
        return

    index = -1
    start = len(dy) + 1
    for j in range(start, up_to + 1):
        index += 2 if j % 2 == 0 else 1
        dy[j] = dy[1] * j - 2 * index

calculate_values(10**6)  # 초기에 필요한 값들을 미리 계산

for _ in range(T):
    case = int(input())
    calculate_values(case)  # 필요한 값까지 계산
    result = dy[case]
    print(result)
