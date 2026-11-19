
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

highest_expense = max(expenses)
index = expenses.index(highest_expense)

print("Most expensive category:", categories[index])
print("Amount:", highest_expense)
