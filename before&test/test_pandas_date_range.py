import datetime
import pandas as pd

today = datetime.date.today()
days = 5
target_day = today-datetime.timedelta(days=days)

date_range = pd.date_range(start=target_day, end=today)

print(date_range)
print(len(date_range))


list_range = list(date_range)

# print(list_range[0])
# print(list_range[0].strftime('%y.%m.%d.'))
# print(list_range[3].strftime('%y.%m.%d.'))

day_list = []
for i in range(0, days+1):
    day_list.append(date_range[i].strftime('%y.%m.%d.'))
    
# print(len(day_list))
print(day_list)

