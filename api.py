# api-key is 6c90e83eea0a47679901d643aae7682e
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6c90e83eea0a47679901d643aae7682e



import requests



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
#PARAMS = {'q':searchquery, 'apiKey':apiKey} 




def sourcesA(): 
	r = requests.get(url = baseURL+endpoint_sources, params = PARAMS) 
	data = r.json(); 
	print(data)
  




def top_headlines():
	r = requests.get(url = baseURL+endpoint_topheadlines, params = PARAMS) 
	data = r.json();
	print(data)





def newsall():
	r = requests.get(url = baseURL+endpoint_everything, params = PARAMS) 
	data = r.json();
	print(data)

  


choice = input("sources, top_headlines, all news");
if choice == "sources":
	sourcesA();
elif choice == "top_headlines":
	top_headlines();
elif choice == "all news":
	newsall();
else: 
	print("Nope go again");


  



