https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

calendar.setfirstweekday(calendar.SUNDAY)

month, day, year = map(int, input().split())
week_day = calendar.weekday(year, month, day)

print(str.upper(calendar.day_name[week_day]))
