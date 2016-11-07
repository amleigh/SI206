import tweepy
from textblob import TextBlob
# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

access_token = "55384204-2U7JpuQPBXwn1SLksxFm1xIOXlWXHFa2myBjyZ0FC"
access_token_secret = "6LngNVVSaNNdbGx9470fQwmO7se7sCtEO6AFBZ6t8DOYX"
consumer_key = "dqdlGvMo7XZ018QMyMwTIWDNu"
consumer_secret = "KjGonAhjMjvfQw4BW85fuitYIJFGSrlGUZYYddnmIg0zH6JWIH"



auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("friends")

subjectivity=[]
polarity=[]


for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	subjectivity.append(analysis.sentiment.subjectivity)
	polarity.append(analysis.sentiment.polarity)
	print(analysis.sentiment)

sub_av= sum(subjectivity)/len(subjectivity)
pol_av= sum(polarity)/len(polarity)

print("Average subjectivity is " + str(sub_av))
print("Average polarity is " + str(pol_av))
