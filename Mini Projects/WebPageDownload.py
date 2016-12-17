#! python2

#   A program to download webpages and saving them to local harddisk 
#	using requests library 

import requests,os

url = 'https://automatetheboringstuff.com/files/rj.txt'

# res is the response object returned by the request.open method, 
# it needs to be checked for errors in downloading. 

res = requests.get(url)

# print(type(res))

# Checks the status code of the response

# print(res.status_code==requests.codes.ok)   

# or using inbuilt method , can also be 
# can also be used in a try except block if failed request is not a deal breaker

res.raise_for_status()

# dealing with text returned 

# print(len(res.text))


# Printing received text is giving encoding error, needed to look into it. 
# Instead of using res.text[:150] , we can use res.content[:250] to avoid encoding error. ERROR resolved :) :) 

# print(res.content[:250])

# saving to harddisk

rj = open("RomioJuliet.txt","wb")

for chunk in res.iter_content(100000):
	rj.write(chunk)
rj.close()

# Opening the saved file
os.system("RomioJuliet.txt")
