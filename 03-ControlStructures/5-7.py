number = int(input("Enter number: "))

words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

while number > 0:
    if number <= 5:
        print(words[number])
    else:
        print(number)

    number -= 1

print("0")