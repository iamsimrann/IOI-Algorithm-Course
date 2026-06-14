# ================================
#  MY CLIMATE TRACKER
#  File: my-climate-tracker.py
# ================================


# PART 1 - USER INPUT
location = input("Enter your location: ")
temperature = float(input("Enter the current temperature in C: "))


# PART 2 - if STATEMENT
if temperature > 35:
    print("Alert: The temperature is extremely high today!")


# PART 3 - if-else
if temperature > 25:
    print("Perfect weather for outdoor activities!")
else:
    print("Consider wearing something warm outside!")


# PART 4 - if-elif-else
if temperature > 35:
    print("Condition: Extremely Hot")
elif temperature > 25:
    print("Condition: Pleasant and Sunny")
elif temperature > 15:
    print("Condition: Mild and Comfortable")
else:
    print("Condition: Chilly - keep yourself warm!")


# PART 5 - datetime MODULE
import datetime
import calendar

current_time = datetime.datetime.now()
print("Location:", location)
print("Current time:", current_time)

print(calendar.calendar(current_time.year))