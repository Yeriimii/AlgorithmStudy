month, day, year, HHMM = input().split()
day = int(day.replace(",", ""))
year = int(year)
HH, MM = map(int, HHMM.split(":"))
cal_month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
cal_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    cal_day[1] += 1
total_time = sum(cal_day) * 24 * 60

current_month = cal_month.index(month)
current_time = (sum(cal_day[:current_month]) + day - 1) * 24 * 60 + HH * 60 + MM
print(current_time / total_time * 100)
