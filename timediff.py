import datetime
date1 = input()
date2 = input()
# datetime(year, month, day, hour, minute, second)
a = datetime.datetime.strptime(date1, "%Y-%m-%d  %H:%M:%S")
b = datetime.datetime.strptime(date2, "%Y-%m-%d  %H:%M:%S")

# returns a timedelta object
c = b-a
print(c)
