# api-key is 6c90e83eea0a47679901d643aae7682e
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6c90e83eea0a47679901d643aae7682e



import requests
import os
import tkinter as tk
from tkinter import * 

pagestart = """

<!DOCTYPE html>
<html>



<head>

  <title>IG-SA</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <script src="./lib/jquery-3.4.1.min.js" onload="window.$ = window.jQuery = module.exports;"></script>
 

<style type="text/css">
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600);



body {
  background: #ededeb;
}
body .title {
  width: 600px;
  margin: 0 auto;
  text-align: center; 
}
body .title h1 {
  margin: 0px 0px 0px 0px;
  font-family: 'Source Sans Pro', sans-serif;
  font-weight: 400;
  color: #FFFFFF; 
}
body .title p {
  margin: 10px 0px 0px 0px;
  font-size: 18px;
  color: #8b8b8b;
  font-weight: 400;
  font-family: 'Source Sans Pro', sans-serif;
}
body .ui {
  width: 450px;
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
  width: 450px;
  height: 240px;
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
  width: 160px;
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



.popupo {
  font-family: "Helvetica Neue", sans-serif;
  width: 100%;
  color: #666666;
  text-align: center;;
}

.popupo .popup-overlay {
  /*Hides pop-up when there is no "active" class*/
  visibility: hidden;
  position: fixed;
  background: #ffffff;
  border: 3px solid #666666;
  width: 73%;
  height: 90%;
  left: 25%;
  z-index: 30;
}



.popupo .popup-overlay.active {
  /*displays pop-up when "active" class is present*/
  visibility: visible;
  text-align: center;
  z-index: 30;
}

.popupo .popup-content {
  /*Hides pop-up content when there is no "active" class */
  visibility: hidden;
  z-index: 30;
}

.popupo .popup-content.active {
  /*Shows pop-up content when "active" class is present */
  visibility: visible;
  z-index: 30;
}

.popupo button {
  display: inline-block;
  vertical-align: middle;
  border-radius: 30px;
  margin: .20rem;
  font-size: 1rem;
  color: #666666;
  background: #ffffff;
  border: 1px solid #666666;
  z-index: 30;
}

.popupo button:hover {
  border: 1px solid #666666;
  background: #666666;
  color: #ffffff;
  z-index: 30;
}



.ui_box button{
  border-radius: 10px;
  font-size: 13px;
}







</style>





</head>




<body>







<div class="title">
  <h1 id = username>
    Username
  </h1>
  <p id = finalValue>Final value statistic</p>
</div>
 




"""



pageend = """

     

</body>
</html>
"""



box = """

<div class="ui">



  <div class="ui_box" id = "boxnumber1">
    <div class="ui_box__inner">
      <h2 id = text1>
        Message Unavailable
      </h2>
      <p id = sender1>---</p>
      <div class="stat">
        <span id = rating1>---</span>
      </div>
      <div class="progress" id = "removearea1">
        <div class="progress_bar" id = "bar1"></div>
      </div>
      <button id = "button1" onclick="openpopupo(9)"></button>
    </div>
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

notify("NewsProvider", "NewsProvider 2.0.0 has been started")



root = tk.Tk();
title = tk.Label(root, text = "NewsProvider 2.0.0", fg = "black", font = ("Courier", 44) );





























  



