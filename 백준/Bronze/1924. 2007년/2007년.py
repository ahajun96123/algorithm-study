month, day = map(int, input().split())
l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(week[(sum(l[:month-1])+day-1)%7])