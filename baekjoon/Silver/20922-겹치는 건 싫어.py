from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    memory = dict()
    answer = 1
    tmp = deque()
    for i in range(n):
        memory[arr[i]] = memory.get(arr[i], 0) + 1
        tmp.append(arr[i])
        if memory[arr[i]] > k:
            while tmp:
                num = tmp.popleft()
                memory[num] -= 1
                if num == arr[i]:
                    break
        answer = max(answer, len(tmp))
    print(answer)
