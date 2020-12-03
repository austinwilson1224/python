import pandas as pd

# importing  the data 
politifact_fake = pd.read_csv('199/data/politifact_fake.csv')
politifact_real = pd.read_csv('199/data/politifact_real.csv')

gossip_cop = pd.read_csv('199/data/gossipcop_fake.csv')
gossip_cop_real = pd.read_csv('199/data/gossipcop_real.csv')



# looking at shape and columns 
politifact_fake.shape # 432 pieces of news  (fake)
politifact_real.shape # 624 pieces of news (real)

politifact_fake.columns
politifact_real.columns

# taking a look at the data
politifact_fake.head()
politifact_real.head()


# number of tweets in the first piece of data 
len(politifact_fake.iloc[0].tweet_ids.split('\t'))

# 'id', 'news_url', 'title', 'tweet_ids' 

news_url_fake = politifact_fake.news_url
len(news_url_fake)


import tweepy 
import json 





'''
FROM THE OTHER TUTORIAL  I WAS  DOING 
'''

# https://www.youtube.com/watch?v=ae62pHnBdAg&t=30s
import tweepy

consumer_key = "SfH6LhmYyWltgdlTFuEm3ODvr"
consumer_secret = "WfzZyfovKaKuhjPV1EGGlTF9ha5zxuTGjIQIgdQ96GicdLyfxY"
access_token = "1311486910322286592-yXQQ8l6IPmexbdK5gBgGGyo3QL7ZVR"
access_token_secret = "U84aUFUgge2MLonznCKd3bodRedwT8bBi4NO6fAe2sHhP"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user("twitter")
# print(user.screen_name)
# print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)


oscar = api.get_user("OscarTheGrouch")
trump = api.get_user("DonaldTrump")
trump.followers_count
print(oscar.screen_name)
print(oscar.followers_count)

public_tweets = api.home_timeline()
public_tweets
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))


api.search("covid")