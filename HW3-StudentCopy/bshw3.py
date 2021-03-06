import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

url= 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


new= soup.prettify()
new=new.replace("student", "AMAZING student")
new=new.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", 'soloshot.jpg')


new=new.replace('logo2.png', 'media/logo.png')
		

f = open('new_webpage.html', 'w')
f.write(new)
f.close()

