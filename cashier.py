def main():
	# write code here
	items = {"name":"","price":"","quantity":""}
	items_list = []
	while items['name'] != "done":
		item = input("enter item name and 'done' when finished :")
		if item == "done".lower():
			break
		else:
			price = float(input("enter the price :"))
			quantity = float(input("Enter the quantity :"))
			items_list.append({"name":item, "price" : price, "quantity":quantity})

	print()
	print("-------------------")
	print("receipt")
	print("-------------------")
	print()


	for i in items_list:
		print(str(i["quantity"]) +" " + i["name"] + " " +str(i["quantity"]*i["price"]))

	print("-------------------")
	x = 0
	for i in items_list:
		x += i["quantity"]*i["price"]
	print(f"The total amount is {x}")
	print("-------------------")


if __name__ == '__main__':
	main()
