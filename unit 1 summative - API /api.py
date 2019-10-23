# api-key is 6c90e83eea0a47679901d643aae7682e
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6c90e83eea0a47679901d643aae7682e



import requests
import os
import tkinter as tk
from tkinter import * 


# api-endpoints
baseURL = "https://newsapi.org"
endpoint_sources = "/v2/sources"
endpoint_everything = "/v2/everything"
endpoint_topheadlines = "/v2/top-headlines"

# params here 
searchquery = ""
country = "";
category = "";
sources = "";
pagesize = "";
apiKey = "6c90e83eea0a47679901d643aae7682e"; 


data = "";




# defining a params dict for the parameters to be sent to the API 
PARAMS = {'apiKey':apiKey} 







#write the html file
def writefile():
	print("jace")






def sourcesA(PARAMS): 
	r = requests.get(url = baseURL+endpoint_sources, params = PARAMS) 
	data = r.json(); 
	writefile();
  




def top_headlines(PARAMS):
	r = requests.get(url = baseURL+endpoint_topheadlines, params = PARAMS) 
	data = r.json();
	print(data)




def newsall():
	r = requests.get(url = baseURL+endpoint_everything, params = PARAMS) 
	data = r.json();
	print(data)

  




def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))



#notify("Title", "Heres an alert")

notify("NewsProvider", "NewsProvider 1.0.0 has been started")


choice = input("Select one of the following requests: Sources, Top Headlines or All News (type help for a description of each: ")

loopbool = 0;
loopbool2 = 0;
loopbool3 = 0;
invalid = 0;
helpp = 0



while loopbool==0: 
	if invalid == 1:
		choice = input("\nInvalid choice, retry: ")
		invalid = 0;
	if helpp == 1:
		choice = input("Select one of the following requests: Sources, Top Headlines or All News (type help for a description of each: ")
		helpp = 0;

	if choice.lower() == "sources":
		PARAMS = {'apiKey':apiKey} 
		sourcesA(PARAMS);
		loopbool = 1;



	elif choice.lower() == "top headlines":
		while loopbool2 == 0: 
			paramsTH = input("\n\n\nEnter a parameter you would like to search using (print help for a list of params): ")

			if paramsTH == "help":
				print("\nPossible Parameters: country, category, source, keywords");



			elif paramsTH.lower() == "country":
				while loopbool3 == 0: 
					countrychoice = input("\nEnter the country selection code (print help for a list of country selection codes): ");
					if countrychoice.lower() == "help": 
						print("\nThe 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options:	ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za")
					else: 
						PARAMS = {'country':countrychoice, 'apiKey':apiKey} 
						top_headlines(PARAMS);
						loopbool = 1;
						loopbool2 = 1;	
						loopbool3 = 1;


			elif paramsTH.lower() == "category":
				while loopbool3 == 0:
					category = input("\nEnter the chosen category query (print help for a list of valid categories): ");
					if category.lower() == "help": 
						print("\nPossible options: business entertainment general health science sports technology")
					else: 
						PARAMS = {'category':category, 'apiKey':apiKey} 
						top_headlines(PARAMS);
						loopbool = 1;
						loopbool2 = 1;
						loopbool3 = 1;

			elif paramsTH.lower() == "source":
				while loopbool3 == 0:
					category = input("\nEnter the chosen source query (print help for a list of valid sources): ");
					if category.lower() == "help": 
						print("\nRestart the program and choose the _sources_ request to see a page with all possible sources.")
					else: 
						PARAMS = {'sources':category, 'apiKey':apiKey} 
						top_headlines(PARAMS);
						loopbool = 1;
						loopbool2 = 1;
						loopbool3 = 1;

			elif paramsTH.lower() == "keywords":
				category = input("\nEnter the chosen keyword query: ");
		
				PARAMS = {'q':category, 'apiKey':apiKey} 
				top_headlines(PARAMS);
				loopbool = 1;
				loopbool2 = 1;














	elif choice.lower() == "help":
		print("\nSources: This endpoint returns the subset of news publishers that top headlines (/v2/top-headlines) are available from. \nThis endpoint provides live top and breaking headlines for a country, specific category in a country, single source, or multiple sources. \nAll news: Search through millions of articles from over 30,000 large and small news sources and blogs. This includes breaking news as well as lesser articles.\n")
		helpp = 1;
	else: 
		invalid = 1;









  



