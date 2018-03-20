import webbrowser
import os
#Launch website and input url 
UrlInput = input('Enter URL')

webbrowser.open (UrlInput)
UrlInput_2= ("www.espn.com")


#Check input from user 
if UrlInput == UrlInput_2:
    print('This is ESPN browser Hurray!')
if UrlInput != UrlInput_2:
    print('This is not ESPN browser')

#Scrap websites (need to research library to import BeautifulSoup or Lxml)
#Closing webbrowser
