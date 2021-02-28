from datetime import datetime
now = datetime.now()

print(now)

print(now.year)
print(now.day)
print(now.month)
print(now.strftime("%d:%m:%Y %H:%M"))