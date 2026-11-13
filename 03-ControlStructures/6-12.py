quantity = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if quantity <= 2:
    total = quantity * price
else:
    full_price = 2 * price
    discounted = (quantity - 2) * price * 0.75
    total = full_price + discounted

print(f"Amount to pay: {total:.2f}")