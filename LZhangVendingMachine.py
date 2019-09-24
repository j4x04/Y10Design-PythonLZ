'''
Vending Machine Project 
Leo Zhang 
UCC
'''

print("Options: \n1: Water - $8 \n2: Granola Bar - 3$ \n3: Fruit Cup - 5$ \n4: Bread - 5$ \n");


kim = 0;
skip = 0;
newitem = 0;
globalremainingmoney = 0;


while(kim == 0): 
	cost = 0;
	if(newitem == 0): 
		cost = input("Input amount of money in dollars: ")
		try:
		    cost = int(cost)
		except ValueError:
		    skip  = 1
	else: 
		cost = globalremainingmoney;
		print("You have " + str(cost) + " dollars left.")
		yesornopt2 = input("Would you like to add money? (y/n)");
		if(yesornopt2 == "y"):
			secondcost = input("How much money do you want to add: ");
			try:
			    secondcost = int(secondcost)
			    print("You now have " + str(cost) + " dollars");
			except ValueError:
				skip = 1;
		else: 
			print("ok, continue ")






	if(skip == 0):
		food = input("Enter your food selection: ")

		
		if(food == "1" or food.lower() == "water"):
			if(int(cost) >= 8):
				print("You have bought water!")
				yesorno = input("Would you like to buy another item? (y/n)");
				if(yesorno == "y"):
					print("Okay, restocking vending machine.....")
					globalremainingmoney = cost-8;
					newitem=1;
				else: 
					print("Thank you for your time. ")
					exit();
			else: 
				print("You have insufficient money")

		elif(food == "2" or food.lower() == "granola bar"):
			if(int(cost) >= 3):
				print("You have bought a granola bar!")
				yesorno = input("Would you like to buy another item? (y/n)");
				if(yesorno == "y"):
					print("Okay, restocking vending machine.....")
					cost = cost-2;
					globalremainingmoney = cost-2;
					newitem=1;
				else: 
					print("Thank you for your time. ")
					exit();
			else: 
				print("You have insufficient money")


		elif(food == "3" or food.lower() == "fruit cup"):
			if(int(cost) >= 5):
				print("You have bought a fruit cup!")
				yesorno = input("Would you like to buy another item? (y/n)");
				if(yesorno == "y"):
					print("Okay, restocking vending machine.....")
					globalremainingmoney = cost-5;
					newitem=1;
				else: 
					print("Thank you for your time. ")
					exit();
			else: 
				print("You have insufficient money")

		elif(food == "4" or food.lower() == "bread"):
			if(int(cost) >= 5):
				print("You have bought bread!")
				yesorno = input("Would you like to buy another item? (y/n)");
				if(yesorno == "y"):
					print("Okay, restocking vending machine.....")
					globalremainingmoney = cost-5;
					newitem = 1;
				else: 
					print("Thank you for your time. ")
					exit();
			else: 
				print("You have insufficient money")


		else: 
			print("Invalid Choice");

	else: 
		print("Invalid amount of money");
		skip = 0;