import utime

# Get the current time as seconds since the epoch (January 1, 1970)
current_time = utime.time()

# Convert seconds since the epoch to a tuple representing local time
local_time = utime.localtime(current_time)

# Print the local time tuple
print("Local Time:", local_time)

# Access individual components of the local time tuple
year, month, day, hour, minute, second, weekday, yearday = local_time
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
print("Weekday:", weekday)
print("Year Day:", yearday)
