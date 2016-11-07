import tweepy
import json
import requests
import urllib.request, urllib.parse, urllib.error

# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
access_token = "55384204-2U7JpuQPBXwn1SLksxFm1xIOXlWXHFa2myBjyZ0FC"
access_token_secret = "6LngNVVSaNNdbGx9470fQwmO7se7sCtEO6AFBZ6t8DOYX"
consumer_key = "dqdlGvMo7XZ018QMyMwTIWDNu"
consumer_secret = "KjGonAhjMjvfQw4BW85fuitYIJFGSrlGUZYYddnmIg0zH6JWIH"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

image= 'http://www.publiusforum.com/images/vote_today.jpg'
#request= requests.get(image)
html = urllib.request.urlopen(image).read()
new_tweet= api.update_with_media(filename='vote_today.jpg', status="#UMSI-206 #Proj3")

#new=api.update_status(new_tweet)
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

#https://upload.twitter.com/1.1/media/upload.json

