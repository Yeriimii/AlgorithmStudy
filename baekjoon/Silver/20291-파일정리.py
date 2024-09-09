import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input().rstrip())
    answer = dict()
    for _ in range(n):
        file_name = input().split(".")[1].strip()
        if file_name in answer:
            answer[file_name] += 1
        else:
            answer[file_name] = 1

    for key in sorted(answer.keys()):
        print(key, answer[key])
