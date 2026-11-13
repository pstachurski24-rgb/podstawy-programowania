pin = "1234"

entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    print("PIN correct")
else:
    print("Incorrect PIN")

new_pin = input("Enter new PIN: ")

if len(new_pin) == 4 and new_pin.isdigit():
    pin = new_pin
    print("PIN changed")
else:
    print("PIN must contain exactly 4 digits")