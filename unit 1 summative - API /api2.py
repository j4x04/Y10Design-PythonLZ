# api-key is 6c90e83eea0a47679901d643aae7682e
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6c90e83eea0a47679901d643aae7682e



import requests
import os
import tkinter as tk
from tkinter import * 


open("main.html", "w").close()


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
    News!
  </h1>
</div>
 
<div class="ui">



"""



pageend = """
</div>
     

</body>
</html>
"""



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




# defining a params dict for the parameters to be sent to the API 
PARAMS = {'apiKey':apiKey} 




















#write the html file
def writefile(jsonfile):
	myfile = open("main.html","a") # use "a" to "append"
	myfile.write(pagestart);

	if jsonfile["status"] != "ok":
		myfile = open("errorpage.html","w") # use "a" to "append"
		myfile.write("<h1>Error, please try again</h1>")
		myfile.close()
	    #OPEN IT
	for val in jsonfile['articles']:
		myfile.write('<div class="ui_box" id = "boxnumber1">');
		myfile.write('<div class="ui_box__inner">')
		myfile.write('<h2 id = text1> ' + str(val["title"]) + ' </h2>');
		myfile.write('<p id = sender1>' + str(val["author"]) + '</p>')
		myfile.write('<p id = sender1>' + str(val["description"]) + '</p>')
		myfile.write('<button id = "button1" value = \'' + val["source"]["name"] + ' \'	  onclick="location.href=\' ' + val["url"] + '\' "></button>')
		myfile.write('</div>');
		myfile.write('</div>');
	myfile.write(pageend);





















def sourcesA(PARAMS): 
	r = requests.get(url = baseURL+endpoint_sources, params = PARAMS) 
	data = r.json(); 
	writefile();
  





def opentopheadlineparams():

	top = Toplevel();

	btn4 = tk.Button(top, text = "Search", font = ("Arial", 20, "bold"));
	btn4.config(height = 3, width = 10);
	btn4.grid(column = 2, row = 5)

	entr = tk.Entry(top)
	entr.grid(column = 2, row = 4)






	def search(anotherparam):
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







	def parameterselect(whichparam): 
		title.config(text = whichparam);
		if whichparam == "country":
			instructions.config(text = "Enter the 2-letter ISO 3166-1 code of \nthe country you want to get headlines for. \nPossible options:	ae ar at au be bg br ca ch cn co cu cz de \neg fr gb gr hk hu id ie il in it jp kr \nlt lv ma mx my ng nl no nz ph pl pt ro rs ru sa \nse sg si sk th tr tw ua us ve za")
			btn4.config(command = lambda: search("country"))
		elif whichparam == "category":
			instructions.config(text = "Enter one of the following categories: \nPossible options: business entertainment general health \nscience sports technology")
			btn4.config(command = lambda: search("category"))
		elif whichparam == "source":
			instructions.config(text = "Restart the program and choose the _sources_ \nbutton to see a page with all possible sources.");
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


		





















def top_headlines(PARAMS):
	r = requests.get(url = baseURL+endpoint_topheadlines, params = PARAMS) 
	data = r.json();
	writefile(data);





def newsall():
	r = requests.get(url = baseURL+endpoint_everything, params = PARAMS) 
	data = r.json();
	print(data)

  




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




btn6 = tk.Button(root, text = "All News",  font = ("Arial", 20, "bold"))
btn6.config(height = 3, width = 10)
btn6.grid(column = 3, row = 2)

#text box
storyline = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
storyline.config(state = "disabled")
storyline.grid(column = 2, row = 3)



















root.mainloop();




















  



