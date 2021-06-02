
# Importing Time Module
import time

# Delaration of Database Variable with some Initializations. 

	# The Database holds the items in stock with price and number available, note; extension of item is available which can be done only by the admin.
items_store={}
items_store['Milk']={'Price': '#150',
										'Available_in_stock' : 200,
										}
items_store['Milo']={'Price': '#1000',
										'Available_in_stock' : 200,
										}
										
items_store['Water']={'Price': '#120',
										'Available_in_stock' : 200,
										}
# The admin information to login to item creation page, the Username is 'Admin' while the password is '12345'										
owner = {'Admin' : '12345'}


# Home page 
print('\t\t WELCOME TO SCHOLAR NURTURE MINI SUPERMARKET \n ')
print('Ready to serve you 24/7 \n')
print('List of what we have in stock are below:\n')

# Some global declaration
total_price = 0
Item_bought = {}

# Login Function
def login():
	"""
	This function deals with log-in of the Admin 
	with the password to be able to add more items to the stock if not available.
	"""
	global owner
	admin=input('You must be an Admin to have access to this page, are you? yes or no : ').lower()
	if admin == 'yes':
		
		print('\n Welcome to Admin Page, You must login before you can add to stock \n Please Login here : ')
		username = input('Type username : ')
		password = input('Type password : ')
		if (username in owner) and (password == owner[username]) :
			print('Login Successful !')
			add_stock()
			print()
			print('List of Available Items in Stock \n')
			supermarket()
		else:
			print('Invalid Login Parameters!')
			shopping = input('Do you want to continue shopping ; yes or no ? : ').lower()
			if shopping == 'yes':
				print('List of Available Items in Stock \n')
				supermarket()
	else:
		print('\nYou cannot have Item to the stock')
		print('\n List of Available Items in Stock \n')
		supermarket()
		
def supermarket():
	"""
	This function deals with most part of the program, it implement the functionalities of other functions in the program.
	
	Other functions it does includes:
		1.  Calculating the price of item purchased by customers.
		2. Issueing Invoices
		3. And many more.
	
	"""
	global items_store,total_price,Item_bought
	
	
	for i in items_store.keys():
		print(f'{i}')
	print("\n (You can add new goods by typing it's name instead of the above name listed.)")								
	selected_item = input('Type what you want to buy please : ').title()
	if selected_item in items_store:
		print('Details of selected Item are :\n')
	
		print(f"{items_store[selected_item]}\n")
		to_buy= input('How many do you want to buy? : ')
		if int(to_buy) <= (items_store[selected_item]['Available_in_stock']):
			items_store[selected_item]['Available_in_stock']-=int(to_buy)
			Item_bought[selected_item]=int(to_buy)
			
			values = int(to_buy)* int(items_store[selected_item]['Price'][1:])
			total_price +=values
		
	
			print(f"{items_store[selected_item]}")
			while True:
				option = input('Do you want to buy more ,  Yes or No ? : ').lower()
			
				if option == 'yes':
					
					supermarket()
				elif option == 'no':
					print(f'Your Total Cost is #{total_price}.00')
					print('Wait for receipt')
					receipt()
					break
				else:
					while True:
						print('Wrong input , please re-select ')
						option = input('Do you want to buy more ,  Yes or No ? : ').lower()
						if option == 'yes' or option =='no':
							if option == 'yes':
								supermarket()
								break
							elif option == 'no':
								print(f'Your Total Cost is #{total_price}.00')
								print('Wait for receipt')
								receipt()
								break
				break
		
				
		else:
			print('Out of stock! \n Reduce your items or shop another item : ')
			print()
			print('List of Available Items in Stock \n')
			supermarket()
		
	else:
		print('Item not found in stock!')
		adds= input('Do you want to add Item to stock ; yes or no ? : ').lower()
		if adds == 'yes':
			login()
		
		else:
			print()
			print('List of Available Items in Stock \n')
			supermarket()
		
def add_stock():
	"""
	Adding stock to the database functionality is being handled by this function.
	
	"""
	global items_store
	add = input('Name of Item: ').title()
	amount = input('Price of Item per unit : #')
	stock = int(input('Supply Available : '))
	
	items_store[add] = {'Price' : "#" + str(amount), 'Available_in_stock' : stock } 
	
	print(items_store)
	
def receipt():
	"""
	Function taking care of issueing  receipt to customers after receiving some basics infromation about the purchase from the costomers
		
	"""
	global total_price,Item_bought
	name = input('Please Provide Your Name: ').upper()
	pay=float(input('Enter amount to pay : #'))
	print('Please wait a bit to get you your invoice.........')
	time.sleep(5)
	if pay >= total_price:
		
		print('Your payment was successful')
		if pay>total_price:
			print(f'please have your change of {pay-total_price}')
		print("\n",'-'*65)
		print('\t\t\tReceipt'.upper())
		print('-'*65)
		print(f'Name : {name}\n')
		print('\t\t Item Bought : ')
		for i,j in Item_bought.items():
			print(f' \t{i} : {j} units ')
		print(f'\nAmount Paid : {pay}')
		print(f'Total Cost : {total_price}')
		if pay>total_price:
			print(f'Balance {pay-total_price}\n\n')
		print(f'\t\t\t {time.ctime()}')
		
		print('Thanks for Shopping with Us, See you next time! ')
	else:
		print('Insufficent fund, kindly drop the items and come back next time')
		exit()
		
		
# Invocation of the main function.	
supermarket()
# End of Program

# Coded by Monsuru Lawal.