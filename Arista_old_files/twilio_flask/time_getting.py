from datetime import datetime,timedelta

now = datetime.now()
future_time = now + timedelta(minutes=1)
current_time = now.strftime("%H:%M")
future_time = future_time.strftime("%H:%M")
print("Current Time =", current_time)
print("future time=",future_time)
print(current_time<future_time)
while current_time<future_time:
    now = datetime.now()
    current_time = now.strftime("%H:%M")


print("done")