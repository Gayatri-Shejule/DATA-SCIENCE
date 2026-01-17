import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 5, 17)
print(x)
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
x = datetime.datetime(2022, 12, 25, 10, 30, 45)
print(x.strftime("%Y-%m-%d %H:%M:%S"))