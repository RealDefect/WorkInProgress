import webbrowser
import os
import html

#Launch website and input url 
UrlInput = input('Enter URL')

webbrowser.open (UrlInput)
UrlInput_2= ("www.espn.com")


#Check input from user 
if UrlInput == UrlInput_2:
    print('This is ESPN browser Hurray!')
if UrlInput != UrlInput_2:
    print('This is not ESPN browser')

#Scrap websites 

#Closing webbrowser

