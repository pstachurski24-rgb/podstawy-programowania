# 1-4: Three student objects and three attributes
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}")

student1 = Student("John", 20, "Computer Science")
student2 = Student("Anna", 21, "Economics")
student3 = Student("Marek", 19, "Management")
for student in [student1, student2, student3]:
    student.display()
