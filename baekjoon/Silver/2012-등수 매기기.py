import sys

if __name__ == '__main__':
    n = int(input())
    ranks = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    ranks.sort()
    answer = 0
    for actual_rank, rank in enumerate(ranks, 1):
        answer += abs(actual_rank - rank)
    print(answer)
