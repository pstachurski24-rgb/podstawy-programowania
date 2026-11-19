
def pts_to_grade(points):
    if points >= 18:
        return "Excellent"
    elif points >= 14:
        return "Good"
    elif points >= 10:
        return "Satisfactory"
    else:
        return "Fail"

test_result = 15
final_grade = pts_to_grade(test_result)

print("Points:", test_result)
print("Grade:", final_grade)
