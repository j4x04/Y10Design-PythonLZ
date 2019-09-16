import random
import time



number = 0; 
vaanan = 0;




while vaanan == 0:
	#time.sleep(0.2);
	input("");
	testnumber = random.randint(1,40)
	if(testnumber == 4): 
		number = 0;
	else: 
		number = number + 1;


	if(number == 100): 
		print("you have ascended");
		input("Press Enter to leave");
		exit();
	else: 
		print(number);


















