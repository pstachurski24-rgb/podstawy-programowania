current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))

reduction = (previous_price - current_price) / previous_price * 100

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

if reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction:.0f}%")