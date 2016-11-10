import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
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

def change_web(base_url):
	html = urllib.request.urlopen(base_url).read()
	soup = BeautifulSoup(html, 'html.parser')

	#Part 1
	for words in soup.find_all("student"):
		new= soup.prettify()
		word=re.sub("student", "AMAZING student", new)
		words.replace_with(word)

	#Part 2
	links= soup.find_all('img')
	# for link in links:
	# 	href=link["src"]

	#Part 3
	for lin in soup.find_all('img'):
		lin['src']='media/logo.png'
			

	web= str(soup)
	
	f = open('new_webpage.html', 'w')
	f.write(web)
	f.close()

change_web(url)