price_list = {'T-shirt':19.99,'Jeans':49.99,'Jacket':89.99,'Sneakers':59.99,'Hat':15.99}
def display(prices):
    for product, price in prices.items():
        print(f"{product}: {price:.2f}")
    print(f"Total: {sum(prices.values()):.2f}")
print('Before discount:')
display(price_list)
for product in price_list:
    price_list[product] = round(price_list[product]*0.90,2)
print('After discount:')
display(price_list)
