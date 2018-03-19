import webbrowser
import os
#Launch website and input url 
UrlInput = input('Enter URL')

webbrowser.open (UrlInput)


#interact with website

print('Succesfully opened browser')


#Closing webbrowser
os.system ("taskkill /im iexplore.exe /f")
