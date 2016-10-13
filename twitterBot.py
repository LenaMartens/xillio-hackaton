import tweepy
import sys
import random

# Small script that takes its input and tweets it out with a random trending hashtag
#Check if we have a text to tweet
if len(sys.argv) < 2 or len(sys.argv[1]) < 1:
    print("error")
    exit(1)

file = open('twitter.config', 'r')
consumer_key = file.readline()
consumer_secret= file.readline()
access_token = file.readline()
access_token_secret = file.readline()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# We want trending near hilversum, place of hackaton :o|
nearestPlace = api.trends_closest(lat=52.223756, long=5.176539)

trends = api.trends_place(id = nearestPlace[0]["woeid"])

# Find a random trending hashtag with 20 or less characters
while True:
    most_trending = random.choice(trends[0]["trends"])["name"]
    if(len(most_trending) <= 20):
        break;

api.update_status(status=sys.argv[1] + '  ' +most_trending)
