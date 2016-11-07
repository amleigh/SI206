import tweepy
import nltk

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

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

