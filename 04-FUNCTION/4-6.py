
def day_name(day_number):
    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        return "Invalid day"

print("The name of day 5 is", day_name(5))
print("The name of day 3 is", day_name(3))
print("The name of day 7 is", day_name(7))
