#! python2

# A Program to automatically open Google Maps with address given in cmd line arguments 
# or the clipboard contents

import webbrowser,sys,pyperclip

# if cmd line arguments are given
if len(sys.argv) >1:
	search_address= ' '.join(sys.argv[1:])

# Get address from clipboard
else:
	search_address=pyperclip.paste()


# address to open
base_url="https://www.google.com/maps/place/"
new_url=base_url+search_address
print new_url

# opening the web browser



webbrowser.open(new_url)

