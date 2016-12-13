from datetime import datetime

def num2date(num):
    year = 1990
    month = 1
    day = 1

num = 36119

year = num / 365
month = num / 30
dt = datetime.fromordinal(36119)
print year+1900
print month