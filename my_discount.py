def my_discount(price, discount):
	price = int(input("Enter price: "))
	discount = int(input("Enter discount: "))

	percentage = discount / 100 * price
	result = price - percentage
	return result

print(my_discount(150,15))
