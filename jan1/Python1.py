# Current date and time Display

# 1- Write a Python program to display the current date and time

import datetime

now = datetime.datetime.now()

print("Date and time Present day : ")

print(now.strftime("%Y-%m-%d-%H:-%M:-%S:"))
