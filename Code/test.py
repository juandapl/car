from mimetypes import init
import requests
from datetime import datetime, timedelta
import calendar

newCourse = requests.get("https://schedge.a1liu.com/2020/fa/22502").json()
print(newCourse['name'])

results = []
days = ""


for m in newCourse['meetings']:
    date_time_str = m['beginDate']
    date_time_obj = datetime.strptime(date_time_str, '%Y-%d-%m %H:%M:%S')
    init_time = date_time_obj.time()
    final_time = date_time_obj + timedelta(minutes= m['minutesDuration'])

    days += date_time_obj.strftime('%A') + " "

    print(date_time_obj)
time = init_time.strftime("%H:%M") +"-"+ final_time.strftime("%H:%M")

print(days, time)