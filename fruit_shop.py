fruit_list = {}
cart = {}
def main_menu():
	print ("Choose your option \n")
	print ("1.Add fruit \n")
	print ("2.Delete fruit \n")
	print ("3.Search fruit name and price \n")
	print ("4.Display\n")
	print ("5.Shop \n")
	print ("6.Exit \n")
def add_fruit():
	f_id = input("Enter the ID of fruit to be added\t")
	fruit = input("Enter the fruit to be entered \t")
	rate = int(input("Enter the rate of the fruit \t"))
	origin = input("Enter the country of origin \t ")
	i_date = input("Enter the date of import \t")
	temp = {
			"Name" : fruit,
			"Price" : rate,
			"Imported from" : origin,
			"Import date" : i_date,
	}
	fruit_list[f_id] = temp
def del_fruit():
	show_fruit_list()
	f_id = input("Enter the fruit ID  to be deleted \t")
	if f_id not in fruit_list:
		print ("Invalid ID")
	else:
		del fruit_list[f_id]
def search_fruit_menu():
	print ("\t\tChoose your option ")
	print ("\t\t1.Search by name ")
	print ("\t\t2.Serch by rate ")
	print ("\t\t3.Exit ")
def search_by_name():
	name = input("Enter the fruit to be searched \t")
	
	flag = False
	for i in fruit_list.values():
		if  i["Name"] == name:
			print (f'{i["Name"]} | {i["Price"]} | {i["Imported from"]} | {i["Import date"]}')
def search_by_rate():
	limit = int(input("Enter the price limit you are looking for"))
	flag = False
	for i in fruit_list.values():
		if  int(i["Price"]) <= limit:
			print (f'{i["Name"]} | {i["Price"]} | {i["Imported from"]} | {i["Import date"]}')
	
def search_fruit():
	while True:
		search_fruit_menu()
		choice = input("Enter your option\t")
		if choice == "1":
			search_by_name()
			
		elif choice == "2":
			search_by_rate()
		
		elif choice == "3":
			break

		else:
			print("Invalid input")
	
def show_fruit_list():
	for f_id,o in fruit_list.items():
		print (f'\t\t{f_id} | {o["Name"]} | {o["Price"]} | {o["Imported from"]} | {o["Import date"]}')

def shop_menu():
	print ("\t\tEnter your option ")
	print ("\t\t1.Add to cart ")
	print ("\t\t2.Delete from kart ")
	print ("\t\t3.Show cart ")
	print ("\t\t4.Bill ")
	print ("\t\t5.Exit ")

def add_to_cart():
	print ("Choose the fruits to add to cart \n")
	for i,o in fruit_list.items():
		print (f'{i} | {o["Name"]}')
	f_id = input("Enter the Id of fruits to add to cart")
	for x,y in fruit_list.items():
		if x == f_id:			
			cart[y["Name"]] = (y["Price"])
			
			
def del_from_cart():

	show_cart()
	name = input("\t\tEnter the fruit to be deleted ")
	if name not in cart.keys():
		print ("Invalid ID")
	else:
		del cart[name]
	
def Bill():

	print ("\t\tYour items in cart are")
	show_cart()
	g = cart.values()
	print (f"\t\t The bill amount is  {sum(g)}")

def shop():
	while True:
		shop_menu()
		choice = input("Enter your choice \t")
		a = 1
		if choice == "1":
			add_to_cart()
		
		elif choice == "2":
			del_from_cart()

		elif choice == "3":
			show_cart()

		elif choice == "4":
			Bill()
			
		elif choice == "5":
			break
			
		else:
			print("Invalid input")
def show_cart():
	for i,o in cart.items():
		print ("\t\t"+ i + " " + " : " + str(o) )
while True:
	main_menu()

	choice = input("Enter your choice \t")
	a = 1
	if choice == "1":
		add_fruit()
		
	elif choice == "2":
		del_fruit()

	elif choice == "3":
		search_fruit()

	elif choice == "4":
		show_fruit_list()

	elif choice == "5":
		shop()

	elif choice == "6":
		break
	else :
		print ("Invalid input")
