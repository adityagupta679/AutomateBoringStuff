# AutomateBoringStuff
Implementation of Programming projects examples from [Automate the Boring Stuff with Python.](https://automatetheboringstuff.com/)

##Project List

##Mini Projects

1. __mapIt:__    *A Program to automatically open Google Maps with the address given in cmd line arguments or the clipboard contents.*  
2. __WebPageDownload:__  *A program to download webpages and saving them to local harddisk using requests library.*
  TODO: 
    - [*] Check Encoding Error while printing the webpage received.  
3. __GoogleSearchHelpCLient:__ *A Web scraping program to query google for a search term and open the First few links automatically in the browser . Hence avoiding the trouble to open the links by hand.*                                         
   TODO:
    - [*] Handle issue of youtube links not opening correctly ,mainly an issue of character encoding or conversion.
4. __AutoFacebookLogin:__ *This program helps in automatically signing in to facebook by editing the values of email and password in the fields provided. It uses selenium WebDriver for automation. Can also be used with a few modidications to automatically log in to any site or perhaps to open up a browser with all your favorite sites automatically logged in. You will have to download Chrome Driver and include it in the path for this program to work.*
5. __AutoPlay2048:__ *A Program for automatically playing 2048 game at https://gabrielecirulli.github.io/2048/ . It uses selenium WebDriver for automation. You will have to download Chrome Driver and include it in the path for this program to work.* 
  TODO:
    - [ ] Maybe find a better way of playing and to increase the score.    

__TODO:__
  - [ ] Build a script to autmate login for some common sites like gmail , facebook , twitter etc. using a single script. 
  - [ ] Build a password generation script.
  - [ ] Use the automate login , password generation scripts to build a password management utility script.
 
  
### Running the Scripts.
*You should have python (these programs have been run on python 2.7) installed (setting up a virtualenv is preferrable). After setting it up, 
install the requirements for the scripts using the command:*
```
pip install -r requuirements.txt 
```
*Next download Chrome Driver from [here.](https://sites.google.com/a/chromium.org/chromedriver/ ) (for automatic website interaction scripts) and unzip the driver file in the scripts directory of your Virtualenv.*

*And you are good to go. Enjoy . :) :)* 