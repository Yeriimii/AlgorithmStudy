import heapq

N = int(input())
q = []

cnt = 0
for _ in range(N):
    S, T = map(int, input().split())
    q.append([S, T])

q.sort()

room = []
# 첫 번째 강의실에 첫 강의가 끝나는 시간을 저장
heapq.heappush(room, q[0][1])

# 두 번째 강의실부터 시작
for i in range(1, N):
    # 현재 강의가 끝나는 시간 > 두 번째 강의가 시작하는 시간
    if room[0] > q[i][0]:
        heapq.heappush(room, q[i][1])  # 새 강의실 배정
    else:
        # 현재 강의실 재사용
        heapq.heappop(room)  # 현재 강의실이 비워지는 시간 저장
        heapq.heappush(room, q[i][1])

print(len(room))
