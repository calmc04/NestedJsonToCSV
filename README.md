# NestedJsonToCSV


This program comes from me having a problem with a fun project I was working on, I had a large file of JSON data which needed to be put on an external database, it had to be in CSV format to import. 
Immediately I googled json to csv and tried various websites and got terrible results for example. 
If I put in:

"0":{
	"color":{
	 "r":255.0,
	 "b":255.0,
	 "a":255.0,
	 "g":255.0
	},
	"zoom":0.0,
	"itemID":0.0,
	"desc":"A simple item",
	"canBeBought":false,
	"type":"item",
	"name":"itemnumberone",
}

It would group by each individual branch which isn't what I wanted, I needed it to be grouped by itemID and then the rest goes into another attribute.
So this is why I've created this program you should be able to group by whatever you need or multiple, so if you wanted it to display in my example zoom, you'd just replace
all mentions of itemID with zoom, this should give it it's own column, ideal for "primary keys".

Really yeah not too complicated does largeish files very quickly mine has roughly 2000 of those json examples and it takes about a second or so.