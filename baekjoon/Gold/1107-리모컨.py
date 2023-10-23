if __name__ == '__main__':
    n = int(input())  # 80000
    m = int(input())
    ban = list()
    if m > 0:
        ban = list(map(int, input().split()))

    # +- 버튼으로만 이동했을 때 최소한 눌러야 하는 수
    min_click = abs(100 - n)  # 79900

    for nums in range(1000001):
        nums = str(nums)  # 77777

        for j in range(len(nums)):  # range(0, 5)
            # 고장난 버튼에 속하면 break
            if int(nums[j]) in ban:
                break
            # 고장난 버튼에 속하지 않으면 -> 최소 +- 카운트와 최소값 비교
            elif j == len(nums) - 1:  # 마지막 루프에 도달하면
                # abs(77777 - 80000) + 5자리만큼 버튼 클릭 = 2223 + 5
                min_click = min(min_click, abs(int(nums) - n) + len(nums))

    print(min_click)
