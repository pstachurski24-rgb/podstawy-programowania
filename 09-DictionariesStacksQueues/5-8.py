prices = {'milk':1.49,'butter':2.09,'juice':1.19,'bread':1.99}
cart = {'juice':3,'bread':1,'milk':2}
total = 0
for product, quantity in cart.items():
    cost = prices[product]*quantity
    print(f'{product}: {quantity} x {prices[product]:.2f} = {cost:.2f}')
    total += cost
print(f'Total: {total:.2f}')
