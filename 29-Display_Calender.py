import calendar

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

calendar = calendar.month(year, month)
print(calendar)