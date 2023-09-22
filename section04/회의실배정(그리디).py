n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x : (x[1], x[0]))  # x[1]을 최우선, x[0]을 차선으로 정렬
end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:  # 해당 회의 시작 시간 >= 기존의 끝나는 시간
        end_time = e  # 기존 끝나는 시간을 해당 회의의 끝나는 시간으로 저장
        cnt += 1  # 회의 가능 수 추가
print(cnt)
