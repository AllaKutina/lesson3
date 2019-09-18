"""
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""

from datetime import datetime, date, timedelta
import dateutil.relativedelta

dt_now = datetime.now()
print(dt_now)

dt_yesterday = dt_now - timedelta(days=1)
print(dt_yesterday)

dt_last_month = dt_now + dateutil.relativedelta.relativedelta(months=-1)
print(dt_last_month)

date = '01/01/17 12:10:03.234567'
datetime_object = datetime.strptime('01/01/17 12:10:03.234567', "%d/%m/%y %H:%M:%S.%f")
print(datetime_object)