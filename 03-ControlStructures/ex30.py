import time
hour_24 = input("Enter time (24-hour format): ")
t = time.strptime(hour_24, "%H:%M")
timevalue_12hour = time.strftime( "%I:%M %p", t )
print(f"Time in 12-hour format: {timevalue_12hour}")
 #DO OGARNIECIA