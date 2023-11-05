code = list(map(int, input()))
code_len = len(code)
dy = [0 for _ in range(code_len + 1)]

# 암호 해석 불가
if code[0] == 0:
    print("0")
else:
    code = [0] + code  # 코드의 인덱스 편하게 만들기
    dy[0] = dy[1] = 1
    for i in range(2, code_len + 1):
        if code[i] > 0:  # 현재 자리수가 0보다 클 때
            dy[i] += dy[i - 1]  # 이전 dy 값 붙이기
        temp = code[i - 1] * 10 + code[i]  # 현재 자리수를 두 자리 숫자로 볼 때
        if temp >= 10 and temp <= 26:  # 10~26번 알파벳에 해당하면
            dy[i] += dy[i - 2]  # 전전 dy 값을 붙인다.
    print(dy[code_len] % 1000000)
