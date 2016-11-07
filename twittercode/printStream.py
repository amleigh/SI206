import tweepy
import json

# Unique code from Twitter
access_token = "55384204-2U7JpuQPBXwn1SLksxFm1xIOXlWXHFa2myBjyZ0FC"
access_token_secret = "6LngNVVSaNNdbGx9470fQwmO7se7sCtEO6AFBZ6t8DOYX"
consumer_key = "8ESXWYcgBc2J4nnZEFdHqCHwR"
consumer_secret = "UKUN8ScdyN16bkLrU5QdYdGnBsdES81HLud3OrQUYHIVN47XEt"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


