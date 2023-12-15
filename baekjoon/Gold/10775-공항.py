# G = int(input())
# P = int(input())
# plain_list = dict()
# gate_list = [True for _ in range(G + 1)]
# plain = [int(input()) for _ in range(P)]
# gate_list[0] = False
# is_ending = False
# cnt = 0
# for i in range(P):
#     g = plain[i]
#     plain_gate_list = plain_list.get(g, [])
#     if len(plain_gate_list) == 0 and gate_list[g] == True:
#         plain_gate_list.append(g)
#         plain_list[g] = plain_gate_list
#         gate_list[g] = False
#         cnt += 1
#     else:
#         if len(plain_gate_list) != 0:
#             last_gate_num = plain_gate_list[-1]
#         else:
#             last_gate_num = g - 1
#         for j in range(last_gate_num - 1, 0, -1):
#             if gate_list[j] == True:
#                 plain_gate_list.append(j)
#                 plain_list[g] = plain_gate_list
#                 gate_list[j] = False
#                 cnt += 1
#                 break
#         else:
#             print(cnt)
#             break
# else:
#     print(cnt)

import sys


def find(_airplane):
    # 자기 자신을 가리키거나, 초기화 값이면
    if alters[_airplane] == _airplane:
        return _airplane
    else:
        # 자기 자신이 아니면 대안 게이트(부모)를 찾는다
        x = find(alters[_airplane])
        alters[_airplane] = x
        return alters[_airplane]


def union(a, b):
    # a의 대안 게이트 찾기
    a = find(a)
    # b의 대안 게이트 찾기
    b = find(b)

    if a < b:
        alters[b] = a
    else:
        alters[a] = b


input = sys.stdin.readline
G = int(input())
P = int(input())

# 대안 게이트 = 부모
alters = {i: i for i in range(G + 1)}
airplanes = [int(input()) for _ in range(P)]
ans = 0

for airplane in airplanes:
    # 대안 게이트 찾기
    alter_gate = find(airplane)

    # 가상의 게이트라면 종료
    if alter_gate == 0:
        break

    # 대안 게이트 업데이트
    union(alter_gate, alter_gate - 1)
    ans += 1

print(ans)
