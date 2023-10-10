import sys

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

n = int(sys.stdin.readline())
num_list = list()
num_dict = dict()
for _ in range(n):
    x = int(sys.stdin.readline())
    num_list.append(x)
    num_dict[x] = num_dict.get(x, 0) + 1

num_list = merge_sort(num_list)

bin = list()
maxx = max(num_dict.values())
for k, v in num_dict.items():
    if v == maxx:
        bin.append(k)
bin = merge_sort(bin)
print(int(round(sum(num_list) / len(num_list), 0)))
print(num_list[len(num_list) // 2])
if len(bin) > 1:
    print(bin[1])
else:
    print(bin[0])
print(num_list[-1] - num_list[0])
