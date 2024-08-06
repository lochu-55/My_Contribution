import machine
import utime

rtc = machine.RTC()

# Get the current time as a tuple
current_time = utime.localtime()

# Set the RTC to the current date and time
rtc.datetime((current_time[0], current_time[1], current_time[2], current_time[6]+1, current_time[3], current_time[4], current_time[5], 0))

print("RTC set to current date and time:", rtc.datetime())




# rtc = RTC()
# rtc.datetime((2024, 5, 28, 10, 36, 48, 0, 0))  # set a specific date and time
# print(rtc.datetime())  # get date and time
