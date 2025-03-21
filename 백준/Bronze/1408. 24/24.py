from datetime import datetime, timedelta

a = input()
b = input()

a_datetime = datetime.strptime(a, "%H:%M:%S")
b_datetime = datetime.strptime(b, "%H:%M:%S")

if a_datetime > b_datetime:
    b_datetime += timedelta(days=1)

delta = b_datetime - a_datetime
total_seconds = int(delta.total_seconds())

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
