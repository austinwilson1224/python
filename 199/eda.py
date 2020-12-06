import pandas as pd

# importing  the data 
politifact_fake = pd.read_csv('data/politifact_fake.csv')
politifact_real = pd.read_csv('data/politifact_real.csv')

gossip_cop = pd.read_csv('data/gossipcop_fake.csv')
gossip_cop_real = pd.read_csv('data/gossipcop_real.csv')




# looking at shape and columns 
politifact_fake.shape # 432 pieces of news  (fake)
politifact_real.shape # 624 pieces of news (real)


# drop na values 
politifact_fake.dropna(inplace=True)
politifact_real.dropna(inplace=True)

# look at shape again 
politifact_fake.shape
politifact_real.shape

##################################

cols = politifact_fake.columns
twitter_stuff = ['user_id', 'tweet_text', 'fake']
cols = list(cols)
cols.append(twitter_stuff)
cols

# make a new data frame to add stuff to
df = pd.DataFrame(columns=cols)


###################################
# taking a look at the data
politifact_fake.head()
politifact_real.head()



# storing ids as a list
politifact_fake['tweet_ids_list'] = politifact_fake.tweet_ids.str.split('\t')

politifact_fake['num_tweets'] = politifact_fake.tweet_ids_list.str.len()



j = 0
for i in range(politifact_fake.shape[0]):
    if pd.isna(politifact_fake.tweet_ids.iloc[i]):
        continue
    j += 1
    temp = politifact_fake.num_tweets.iloc[i]
    print(temp, end=" ")

j #  392 entries 



politifact_fake.head()



# 'id', 'news_url', 'title', 'tweet_ids' 

test_data = politifact_fake.iloc[100]
test_tweet_id = test_data.tweet_ids_list[0:20]
# test_tweet_id3 = test_data.tweet_ids_list[3]

test_tweet_id

# stuff

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


result = api.statuses_lookup(id_ = test_tweet_id)

for status in result:
    print("The status " + str(status.id) + " is posted by " + status.user.screen_name) 
    print("This status says : \n\n" + status.text, end = "\n\n") 




x = json.loads(result[2])
result[2].expanded_url
len(result)
result3

type(result)













########################### old stuff from testing

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