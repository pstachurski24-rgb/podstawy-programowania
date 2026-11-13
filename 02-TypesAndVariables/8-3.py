# Celsius -> Kelvin and Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

kelvin = celsius + 273.15
fahrenheit = celsius * 9 / 5 + 32

print(f"Kelvin: {kelvin:.2f}")
print(f"Fahrenheit: {fahrenheit:.2f}")