import tweepy
import sys
import random

# Small script that takes its input and tweets it out with a random trending hashtag
#Check if we have a text to tweet
if len(sys.argv) < 2 or len(sys.argv[1] < 1):
    print("error")
    exit(1)

auth = tweepy.OAuthHandler('GvANtcrg1UqBshL7bR2NrztvL', 'saSGb4tqAgiicIZ9KLfrRIj3TtAs4jw3yueEmb7y9URlBpMYP7')
auth.set_access_token('784743466135846912-FYVuAcC4nLfZA5iN85LsjsRPsnYRAMq', 'E0D5wdU37xic4pIqTFH2q4QvMKaY687jp2DkdwsFoaMFZ')

api = tweepy.API(auth)

# We want trending near hilversum
nearestPlace = api.trends_closest(lat=52.223756, long=5.176539)

trends = api.trends_place(id = nearestPlace[0]["woeid"])

# Find a random trending hashtag with 20 or less characters
while True:
    most_trending = random.choice(trends[0]["trends"])["name"]
    if(len(most_trending) <= 20):
        break;

api.update_status(status=sys.argv[1] + '  ' +most_trending)
