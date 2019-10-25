# api-key is 6c90e83eea0a47679901d643aae7682e
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6c90e83eea0a47679901d643aae7682e



import requests
import os
import tkinter as tk
import webbrowser
from tkinter import * 
import time

open("main.html", "w").close()













# variable with the first half of the html page: head tags, style, all contained here. 
pagestart = """ 

<!DOCTYPE html>
<html>



<head>

  <title>NewsProvider</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
 

<style type="text/css">
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600);



body {
  background-image: linear-gradient(to top right, #A82A71, #4C61B0);
}
body .title {
  width: 800px;
  margin: 0 auto;
  text-align: center; 
}
body .title h1 {
  margin: 0px 0px 0px 0px;
  font-family: 'Source Sans Pro', sans-serif;
  font-weight: 400;
  color: #000000; 
}
body .title p {
  margin: 10px 0px 0px 0px;
  font-size: 18px;
  color: #000000;
  font-weight: 400;
  font-family: 'Source Sans Pro', sans-serif;
}
body .ui {
  width: 750px;
  margin: 0 auto;
  margin-top: 50px;
  font-family: 'Source Sans Pro', sans-serif;
  color: white;
  box-shadow: none;
}
body .ui ul {
  margin: 0px 30px 10px 0px;
  padding: 0;
  list-style-type: none;
  font-size: 11px;
  font-weight: 400;
  line-height: 20px;
}
body .ui .drop p {
  color: #f8fbfa;
}
body .ui_box {
  width: 800px;
  height: 280px;
  position: relative;
  background: #3d3d3d;
  float: left;
  box-shadow: -1px 0px rgba(255, 255, 255, 0.07);
  cursor: pointer;
  transform: scale(1);
  transition-property: transform, background;
  transition-duration: 0.3s;
}
body .ui_box__inner {
  padding: 30px;
}
body .ui_box__inner span {
  font-size: 36px;
  font-weight: 700;
}
body .ui_box__inner .progress {
  width: 100%;
  margin-top: 10px;
  height: 6px;
  background: rgba(0, 0, 0, 0.3);
  margin-bottom: 15px;
}



body .ui_box__inner .progress_bar {
  height: 6px;
  float: left;
  width: 10%; /* THIS IS THE PROGRESS BAR !!!!!!!!! */
  background: #ad1302;
  -webkit-animation: bar 2s;
}
body .ui_box h2 {
  font-weight: normal;
  font-size: 16px;
  margin: -4px 0px 3px 0px;
}
body .ui_box p {
  font-size: 13px;
  color: #b6b6b6;
  clear: left;
  font-weight: 300;
  width: 750px;
  margin: 2px 0px 15px 0px;
}
body .ui_box:hover {
  background: #4fa584;
  transform: scale(1.1);
  transition-property: transform, background;
  transition-duration: 0.3s;
  position: relative;
  z-index: 1;
}
.ui_box:hover > .ui_box__inner p {
  color: #b3dacb;
}
.ui_box:hover > .drop {
  transition-property: bottom, opacity;
  transition-duration: 0.3s;
  bottom: -42px;
  opacity: 1;
}
.ui_box:hover > .drop .arrow {
  transition-property: transform;
  transition-duration: 1s;
  transform: rotate(765deg);
}
.ui_box:hover > .ui_box__inner .progress_graph > div {
  background: white;
}
.ui_box:hover > .ui_box__inner .progress .progress_bar, .ui_box:hover > .ui_box__inner .progress .progress_bar--two {
  background: white;
}
.stat_left {
  float: left;
}






.ui_box button{
  font-size: 13px;
  font-colour: #000000;
}






</style>





</head>




<body>







<div class="title">
  <h1 id = username>
    NewsProvider 2.0 - Made with <a href="https://newsapi.org/">NewsApi</a>
  </h1>
</div>
 
<div class="ui">



"""


#ending of the html page, closing off body, html tags
pageend = """
</div>
     

</body>
</html>
"""




#this var is not used in the program - but this is the format for the boxes with the information displayed in it (this is also the 
#middle of the html code, to be put in between pagestart and pageend)
box = """


  <div class="ui_box" id = "boxnumber1">
    <div class="ui_box__inner">
     


      <h2 id = text1>
        Message Unavailable
      </h2>
 

      <p id = sender1>---</p>


      <button id = "button1" onclick=""></button>
    </div>
  </div>

"""

















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




# defining a params dict for the parameters to be sent to the API, will be changed later depending on request made 
PARAMS = {'apiKey':apiKey} 
































#write the html file
def writefile(jsonfile):
	myfile = open("main.html","a") # use "a" to "append"
	myfile.write(pagestart);

	if jsonfile["status"] != "ok": #if the status of the returned object isn't "ok", then write an error page
		myfile.write('<div class="ui_box" id = "boxnumber1">');
		myfile.write('<div class="ui_box__inner">')
		myfile.write('<h2 id = text1> Error: ' + jsonfile["code"] +  '</h2>');
		myfile.write('<p id = sender1>' + jsonfile["message"] + '</p>')
		myfile.write('</div>');
		myfile.write('</div>');

	
	else: # writes a different html page if there are no returned objects
		if jsonfile["totalResults"] == 0:
			myfile.write('<div class="ui_box" id = "boxnumber1">');
			myfile.write('<div class="ui_box__inner">')
			myfile.write('<h2 id = text1> No Articles Found </h2>');
			myfile.write('</div>');
			myfile.write('</div>');
		else: 		
			for val in jsonfile['articles']: #for each article returned, write a "block" in the html code (it's a div) with the info
				myfile.write('<div class="ui_box" id = "boxnumber1">');
				myfile.write('<div class="ui_box__inner">')
				myfile.write('<h2 id = text1> ' + str(val["title"]) + ' </h2>');
				myfile.write('<p id = sender1>' + str(val["author"]) + '</p>')
				myfile.write('<p id = sender1>' + str(val["description"]) + '</p>')
				myfile.write('<button id = "button1"	 onclick="location.href= \' ' + val["url"] + '\' ">Click to go to article</button>')
				myfile.write('</div>');
				myfile.write('</div>');


	myfile.write(pageend); #finish the writing process
	myfile.close();
	time.sleep(0.5); # added a 0.5 second delay to make sure the page is written before opening it automatically in browser
	url = os.getcwd();
	url = "file://" + str(url) + "/main.html"; # find path for current file, main.html should be in the same directory
	webbrowser.open(url, new=2); #use webbrowser module to automatically open the file
	#chrome = webbrowser.get('chrome');
	#chrome.open(url);


























def sourcesA(PARAMS): # writing the sources page
	r = requests.get(url = baseURL+endpoint_sources, params = PARAMS) 
	data = r.json(); 

	myfile = open("main.html","a") # use "a" to "append"
	myfile.write(pagestart);

	if data["status"] != "ok":
		myfile = open("errorpage.html","w") # use "a" to "append"
		myfile.write("<h1>Error, please try again</h1>")
		myfile.close()

	for val in data['sources']: # for each source returned, write a block in the html code with the contained information 
		myfile.write('<div class="ui_box" id = "boxnumber1">');
		myfile.write('<div class="ui_box__inner">')
		myfile.write('<h2 id = text1> ' + str(val["name"]) + ' </h2>');
		myfile.write('<p id = sender1>' + str(val["id"]) + '</p>')
		myfile.write('<p id = sender1>' + str(val["description"]) + '</p>')
		myfile.write('<button id = "button1" value ="Go to source site"	  onclick="location.href=\' ' + val["url"] + '\' ">Click to go to website</button>')
		myfile.write('</div>');
		myfile.write('</div>');
	myfile.write(pageend);
	url = os.getcwd();
	url = "file://" + str(url) + "/main.html"; # see above, writefile function, for detailed comments (same process, basically)
	webbrowser.open(url, new=2);	
	root.destroy();
























def opentopheadlineparams(): #opening the popup to enter parameters for the top-headlines

	top = Toplevel();

	btn4 = tk.Button(top, text = "Search", font = ("Arial", 20, "bold"));
	btn4.config(height = 3, width = 10); # establish searhc button
	btn4.grid(column = 2, row = 5)

	entr = tk.Entry(top, state = "disabled")
	entr.grid(column = 2, row = 4)# establish the input field






	def search(anotherparam): # configure the parameters for the search before sending to the function that executes the search, closes the window
		#print(anotherparam)
		n = str(entr.get())
		PARAMS = {'apiKey':apiKey} 

		if anotherparam == "country":
			PARAMS.update( {'country' : n} )
		elif anotherparam == "category":
			PARAMS.update( {'category' : n} )
		elif anotherparam == "source":
			PARAMS.update( {'sources' : n} )
		elif anotherparam == "keywords":
			PARAMS.update( {'q' : n} )
		top_headlines(PARAMS)
		top.destroy();
		root.destroy();






	def parameterselect(whichparam):  #changes the title/label with instructions as to what to do for each param 
		entr.config(state = "normal")
		title.config(text = whichparam);
		if whichparam == "country":
			instructions.config(text = "Enter the 2-letter ISO 3166-1 code of \nthe country you want to get headlines for. \nPossible options:	ae ar at au be bg br ca ch cn co cu cz de \neg fr gb gr hk hu id ie il in it jp kr \nlt lv ma mx my ng nl no nz ph pl pt ro rs ru sa \nse sg si sk th tr tw ua us ve za")
			btn4.config(command = lambda: search("country"))
		elif whichparam == "category":
			instructions.config(text = "Enter one of the following categories: \nPossible options: business entertainment general health \nscience sports technology")
			btn4.config(command = lambda: search("category"))
		elif whichparam == "source":
			instructions.config(text = "Click on the main window, then on the \nsources button to see a page with all possible sources.");
			btn4.config(command = lambda: search("source"))
		elif whichparam == "keywords":
			instructions.config(text = "Enter the chosen keyword query: ");
			btn4.config(command = lambda: search("keywords"))





	title = tk.Label(top, text = "Click a Parameter to search using.", fg = "black", font = ("Courier", 20) )
	title.grid(column = 2, row = 0)

	instructions = tk.Label(top, text = "", fg = "black", font = ("Courier", 20));
	instructions.grid(column = 2, row = 1)	

	btn1 = tk.Button(top, text = "Country", font = ("Arial", 20, "bold"), command = lambda: parameterselect("country"));
	btn1.config(height = 3, width = 10)
	btn1.grid(column = 0, row = 4)

	btn2 = tk.Button(top, text = "Category", font = ("Arial", 20, "bold"), command = lambda: parameterselect("category"));
	btn2.config(height = 3, width = 10)
	btn2.grid(column = 1, row = 4)

	btn3 = tk.Button(top, text = "Source", font = ("Arial", 20, "bold"), command = lambda: parameterselect("source"))
	btn3.config(height = 3, width = 10)
	btn3.grid(column = 3, row = 4)


	btn3b = tk.Button(top, text = "Keywords", font = ("Arial", 20, "bold"), command = lambda: parameterselect("keywords"))
	btn3b.config(height = 3, width = 10)
	btn3b.grid(column = 4, row = 4)


		






def top_headlines(PARAMS): # send the request to the param, return
	r = requests.get(url = baseURL+endpoint_topheadlines, params = PARAMS) 
	data = r.json();
	writefile(data);









































def newsall(PARAMS):
	r = requests.get(url = baseURL+endpoint_everything, params = PARAMS) 
	data = r.json();
	writefile(data);

  







def everythingsearch(): #opening the popup to enter parameters for the top-headlines
	PARAMS = {'apiKey':apiKey} 
	top = Toplevel();


	entr = tk.Entry(top)
	entr.grid(column = 2, row = 4)# establish the input field

	title = tk.Label(top, text = "Choose your language", fg = "black", font = ("Courier", 20) )
	title.grid(column = 2, row = 0)

	instructions = tk.Label(top, fg = "black", font = ("Courier", 20), text = "The 2-letter ISO-639-1 code of the language you want to get headlines for. \nPossible options: ar/de/en/es/fr/he/it/nl/no/pt/ru/se/ud/zh. ");
	instructions.grid(column = 2, row = 1)	






	def search2(): 
		labeltext = title.cget("text")
		n = str(entr.get())
		if labeltext == "Choose your language":
			PARAMS.update( {'language' : n} )
			title.config(text = "Enter keywords to search by")
			instructions.config(text = "")
		elif labeltext == "Enter keywords to search by":
			PARAMS.update( { 'q': n})
			newsall(PARAMS);
			top.destroy();
			root.destroy();




	btn4 = tk.Button(top, text = "Search", font = ("Arial", 20, "bold"), command = search2);
	btn4.config(height = 3, width = 10); 
	btn4.grid(column = 2, row = 5)





































def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))



#notify("Title", "Heres an alert")

notify("NewsProvider", "NewsProvider 2.0.0 has been started")



root = tk.Tk();


#Title Label
title = tk.Label(root, text = "NewsProvider 2.0.0", fg = "black", font = ("Courier", 44) )
title.grid(column = 2, row = 0)



SOURCEPARAMS =  {'apiKey':apiKey} 
#Level buttons
level1button = tk.Button(root, text = "Sources", font = ("Arial", 20, "bold"), state = "normal", command = lambda: sourcesA(SOURCEPARAMS))
level1button.config(height = 3, width = 10)
level1button.grid(column = 0, row = 2)



btn4 = tk.Button(root, text = "Top Headlines", font = ("Arial", 20, "bold"), command = opentopheadlineparams)
btn4.config(height = 3, width = 15)
btn4.grid(column = 2, row = 2)




btn6 = tk.Button(root, text = "All News",  font = ("Arial", 20, "bold"), command = everythingsearch)
btn6.config(height = 3, width = 10)
btn6.grid(column = 3, row = 2)

#text box
storyline = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
storyline.config(state = "disabled")
storyline.grid(column = 2, row = 3)



















root.mainloop();




















  



