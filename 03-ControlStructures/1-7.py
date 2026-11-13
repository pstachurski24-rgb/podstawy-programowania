basic_salary = 5000
bonus = 0.30

is_bonus = input("Does employee receive bonus? (Y/N): ") == "Y"

if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print("Basic salary:", basic_salary)
print("Bonus included?", is_bonus)
print("Total salary:", total_salary)