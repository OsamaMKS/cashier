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

			#index +=1


if __name__ == '__main__':
	main()
