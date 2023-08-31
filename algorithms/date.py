from datetime import datetime
from dateutil.relativedelta import relativedelta

today = "2023-08-21"
target = "2023-09-21"


# 문자열 -> datetime
today_dt = datetime.strptime(today, "%Y-%m-%d")
target_dt = datetime.strptime(target, "%Y-%m-%d")
#time_dt = datetime.strptime(target_dt, "%H:%M:%S")   #시:분:초

# datetime -> 문자열
target = datetime.strftime(target_dt, "%Y-%m-%d")

# 날짜 연산
result_dt = target_dt + relativedelta(days=3)
print(datetime.strftime(result_dt, "%Y-%m-%d"))

# 날짜 비교
if today_dt + relativedelta(months=1) == target_dt:
    print("check")

