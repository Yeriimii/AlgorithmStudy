import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = []
    for _ in range(N):
        paper_rank, interview_rank = map(int, input().strip().split())
        scores.append((paper_rank, interview_rank))
    scores.sort()
    cnt = 0
    highest_rank = N + 1
    for _paper_rank, _interview_rank in scores:
        if _interview_rank < highest_rank:
            highest_rank = _interview_rank
            cnt += 1
    print(cnt)
