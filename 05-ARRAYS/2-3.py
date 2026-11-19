
monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

food = 0
transport = 0
utilities = 0
total = 0

for week in monthly_expenses:
    food += week[0]
    transport += week[1]
    utilities += week[2]

    for expense in week:
        total += expense

print("MONTHLY EXPENSES")
print("----------------")
print("Food:", food)
print("Transport:", transport)
print("Utilities:", utilities)

for i in range(len(monthly_expenses)):
    print(f"Week {i + 1}:", sum(monthly_expenses[i]))

print("----------------")
print("TOTAL:", total)
