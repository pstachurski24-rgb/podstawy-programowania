# Height in cm -> feet and inches

cm = int(input("Enter height in cm: "))

total_inches = cm / 2.54
feet = int(total_inches // 12)
inches = int(total_inches % 12)

print(f"I am {cm} cm tall, i.e. {feet} feet and {inches} inches")