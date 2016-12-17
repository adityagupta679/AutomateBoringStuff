#! pyhton2

# A Web scraping program to query google for a search term and 
# open the First few links automatically in the browser . 
# Hence avoiding the trouble to open the links by hand .


import sys,requests, bs4 , pyperclip, webbrowser, urllib

search_term="" 
# Checking cmd line arguments , if none given, 
# consider the text in the clipboard as a search term

if len(sys.argv)>1 :
	search_term=" ".join(sys.argv[1:])
	
else:
	search_term=pyperclip.paste()
# print search_term

base_url="https://www.google.co.in/search?q="
search_url=base_url+search_term

# Quering Google for the term 

search_results= requests.get(search_url)

#  Check for errors while executing the search request.
search_results.raise_for_status()

soup=bs4.BeautifulSoup(search_results.text,"html.parser")
links= soup.select('h3.r a' )

# extract the urls from the links
urls=[]
for link in links :
	href=link.get('href')
	urls.append(href[href.find("q=")+2:href.find("&sa")])

# Decoding the url to replace % values like %3f for / Handling issue of youtube links not working

urls=[urllib.unquote(url).decode('utf8') for url in urls]
print "Openinng Google results for the Search term: {}. \nThe links are: {} ".format(search_term,str(urls))

# open the links in the webbrowser , limiting to 6 results
for url in urls[:6]:
	webbrowser.open(url)

# TODO:
# [*] Handle issue of youtube links not opening correctly ,
# mainly an issue of character encoding or conversion 
# Handled the issue with youtube links by using urllib's decode function






