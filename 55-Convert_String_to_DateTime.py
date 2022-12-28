# How to Convert String to DateTime using Python Codes

# Solution # 1(Using DateTime Module)
from datetime import datetime

date = "Oct 10 2000 10:10AM"
date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(type(date_time))
print(date_time)

# Solution # 2(Using DateUtil Module)
from dateutil import parser
dateTime = parser.parse("Oct 10 2000 10:10AM")
print(type(dateTime))
print(dateTime)