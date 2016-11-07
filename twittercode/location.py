import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "55384204-2U7JpuQPBXwn1SLksxFm1xIOXlWXHFa2myBjyZ0FC"
access_token_secret = "6LngNVVSaNNdbGx9470fQwmO7se7sCtEO6AFBZ6t8DOYX"
consumer_key = "8ESXWYcgBc2J4nnZEFdHqCHwR"
consumer_secret = "UKUN8ScdyN16bkLrU5QdYdGnBsdES81HLud3OrQUYHIVN47XEt"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" geocode:40.6781784,-73.94415789999999,10km')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
