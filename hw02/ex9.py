
weight = int(input("Enter the weight: "))
price = 0

if weight > 10:
    price *= 4.75
elif weight > 6:
    price *= 4
elif weight > 2:
    price *= 3
else:
    price *= 1.5

print('price: ', price)
