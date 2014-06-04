import urllib.request
import re

htmlSource = urllib.request.urlopen("URL Here").read().decode("iso-8859-1")

#print(htmlSource)
linksList = re.findall("<a href=(.*?)>.*?</a>",htmlSource) #play here to customize it


for link in linksList:
    print (link)
