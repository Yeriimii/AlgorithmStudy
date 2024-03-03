import math
import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


# 세그먼트 트리 생성 및 초기화
def make_segment_tree(node, arr, seg, start, end):
    if start == end:  # 리프 노드
        seg[node] = (arr[start], arr[start])  # min, max를 튜플로 저장
        return seg[node]

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    left = make_segment_tree(left_node, arr, seg, start, mid)  # 왼쪽 자식 노드 호출
    right = make_segment_tree(right_node, arr, seg, mid + 1, end)  # 오른쪽 자식 노드 호출

    seg[node] = (min(left[0], right[0]), max(left[1], right[1]))  # 현재 노드의 min, max 저장

    return seg[node]


def query(seg, node, start, end, left, right):
    # node: 현재 노드의 인덱스
    # start, end: 현재 노드가 나타내는 구간
    # left, right: 찾고자 하는 구간

    # 찾고자 하는 구간이 현재 노드가 나타내는 구간과 겹치지 않는 경우
    if right < start or end < left:
        return 2e9, 0  # 초기값 반환 (min은 무한대, max는 0)

    # 찾고자 하는 구간이 현재 노드가 나타내는 구간을 완전히 포함하는 경우
    if left <= start and end <= right:
        return seg[node]

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    left_result = query(seg, left_node, start, mid, left, right)
    right_result = query(seg, right_node, mid + 1, end, left, right)

    return min(left_result[0], right_result[0]), max(left_result[1], right_result[1])


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 세그먼트 트리의 크기 결정
b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
seg = [0 for _ in range(node_n)]

# 세그먼트 트리 생성 및 초기화
make_segment_tree(1, arr, seg, 0, len(arr) - 1)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # idx
    ans = query(seg, 1, 0, len(arr) - 1, a, b)
    print(ans[0], ans[1])
