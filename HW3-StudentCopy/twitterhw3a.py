import tweepy


# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

new_tweet= api.update_with_media(filename='vote_today.jpg', status="Election 2016 #UMSI-206 #Proj3")


print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


