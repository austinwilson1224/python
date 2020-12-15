'''
FIX id column -- DONE 

specify how many tweets you want to gather (provide new content title and how many tweets they want to collect)


add tweetid to dataframe


run for real data 

for each tweet indicate if it is a reply or not (attribute is replyToTweet if its not a reply then its null if it has int id then its a reply) use hasattribuite function
"in_reply_to_status_id_str": null, (example of tweet that is not a reply) -- add one last column to indicate if each tweet is a reply or not


REPORT 
1 -- focus on fake news net , what it is and how we can use this tool, what data this tool gathers looks like
how we use it
data format 

2 -- focus on your rampup and small functions you create on top of their tool 
talk about in code 
user can speficy the id of any news and number of tweets to gather (use default value for number of tweets) 
talk about output data format 
different columns you create and data you gather 
make more user friendly 
get attributes we want 

3 -- talk about the dataset you collected using your tool 
name as fake news net class 
basic analysis of data collected stats analysis average of tweets for fake news and average for real news 
for each type of news on politifact and gossip cop average number of fake/real tweets 
table w/ 4 rows gossip/poitic reral/fake

4 -- reflection 
things to pay attention to in the future ie the request quota 

'''




import pandas as pd
import tweepy
import json 
# importing  the data 
politifact_fake = pd.read_csv('data/politifact_fake.csv')
politifact_real = pd.read_csv('data/politifact_real.csv')

gossip_cop_fake = pd.read_csv('data/gossipcop_fake.csv')
gossip_cop_real = pd.read_csv('data/gossipcop_real.csv')




# looking at shape and columns 
politifact_fake.shape # 432 pieces of news  (fake)
politifact_real.shape # 624 pieces of news (real)

gossip_cop_fake.shape # 5323 pieces of news (fake)
gossip_cop_real.shape # 16817 peices of news (real)


# drop na values 
politifact_fake.dropna(inplace=True)
politifact_real.dropna(inplace=True)

gossip_cop_fake.dropna(inplace=True) 
gossip_cop_real.dropna(inplace=True)

# look at shape again 
politifact_fake.shape # 389 pieces of news 
politifact_real.shape # 373 pieces of news

gossip_cop_fake.shape # 4898 pieces of news (fake)
gossip_cop_real.shape # 15747 peices of news (real)




###################################
# taking a look at the data
politifact_fake.head()
politifact_real.head()



# storing ids as a list
politifact_fake['tweet_ids_list'] = politifact_fake.tweet_ids.str.split('\t')
politifact_fake['tweet_ids'] = politifact_fake.tweet_ids.str.split('\t') # storing it back in the same column it came from? 

politifact_fake['num_tweets'] = politifact_fake.tweet_ids_list.str.len()




# 'id', 'news_url', 'title', 'tweet_ids' 

test_data = politifact_fake.iloc[102]
test_data2 = politifact_fake.iloc[200]
test_data.tweet_ids = test_data.tweet_ids[0:20]
test_tweet_id = test_data.tweet_ids_list[0:20]


len(test_data.tweet_ids)


test_data
test_data2

'''
FROM THE OTHER TUTORIAL  I WAS  DOING 
'''

# https://www.youtube.com/watch?v=ae62pHnBdAg&t=30s


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


# building the function, this is data for testing a single 
news_id = test_data.id
id_list = test_data.tweet_ids_list[:99]
news_url = test_data.news_url
title = test_data.title
result = api.statuses_lookup(id_ = test_tweet_id)



def get_all_tweets_single_news_story(row_data, number_of_tweets = False):
    # , id_list, news_id, news_url, title

    # user can specify how many tweets they want to gather for a single news story 
    id_list = row_data.tweet_ids_list
    if number_of_tweets:
        if (len(row_data.tweet_ids) > number_of_tweets + 1):
            id_list = row_data.tweet_ids[:number_of_tweets + 1]
            print(len(id_list))

    # this block is to account for request limitations of twitter ... will do later or not at all ;) 
    # elif len(row_data.tweet_ids) > 100:
    #     pass
    #     i = len(row_data.tweet_ids) // 100 
    #     tweet_subset = row_data.tweet_ids[:99]
    #     for j in range(i):
    #         tweet_subset = row_data.tweet_ids[j*100:j*100+99]
        
    # else:
    #     id_list = row_data.tweet_ids_list
    news_id = row_data.id 
    news_url = row_data.news_url
    title = row_data.title
    # twitter API call 
    result = api.statuses_lookup(id_ = id_list)

    # these arrays will store the data from the API call
    # df_id_list, news_url_list and title_list will store the same repeated value
    tweet_ids_list = []
    username_list = []
    text_list = []
    news_id_list = []
    news_url_list = []
    title_list = []
    reply_list = []

    # looping through all the tweets gathered from statuses_lookup which was passed a list of tweet ids
    for status in result:
        # this is the ID for each individual tweet
        tweet_id = status.id
        tweet_ids_list.append(tweet_id)
        # username for each individual tweet
        username = status.user.screen_name 
        username_list.append(username)
        # text value for each individual tweet
        text = status.text
        text_list.append(text)
        # 
        reply = status.in_reply_to_status_id_str
        if reply is None:
            reply_list.append(False)
        else:
            reply_list.append(True)
        # these are repeated values: news_id, news_url and title will be the same for all tweets associated with a particular news story (row) 
        news_id_list.append(news_id)
        news_url_list.append(news_url)
        title_list.append(title)
    data = {"news_id": news_id_list, "news_url": news_url_list, "title": title_list, "tweet_id": tweet_ids_list, "username": username_list, "text": text_list, "reply": reply_list}
    return pd.DataFrame(data)



######### testing

test = get_all_tweets_single_news_story(row_data= test_data)#, number_of_tweets = 2)
test.shape
test

test2 = get_all_tweets_single_news_story(row_data = test_data2, number_of_tweets=10)
test2


t3st = politifact_fake.sample(4)
t3st












# now traverse the whole data frame and do this for each row ... 
# columns=["df_id","news_url","title", "id", "username", "text"]



politifact_fake_test = politifact_fake[:10]
politifact_fake_test

def aggregate_data(df, name = "temp.csv", number_of_tweets = False):
    result = pd.DataFrame()
    for row in df.iterrows():
        row = row[1] # because iterrows() gives us a tuple (index, row) 
        news_id = row.id
        # id_ = row.id
        # print(id_)
        id_list = row.tweet_ids_list
        if len(id_list) > 100:
            id_list = id_list[:99]
        news_url = row.news_url
        title = row.title
        # result = api.statuses_lookup(id_ = id_list)
        df2 = get_all_tweets_single_news_story(row_data = row, number_of_tweets = number_of_tweets)
        # print(df2.shape)
        
        result = df.append(df2, ignore_index= True)
    result.to_csv(name)
    return result
    

test4 = aggregate_data(df = t3st, name = "test.csv", number_of_tweets=10)

test4.iloc[1]








politifact_fake_test


df = pd.DataFrame()
politifact_fake_test = politifact_fake.sample(4)
for row in politifact_fake_test.iterrows():
    row = row[1] # because iterrows() gives us a tuple (index, row) 
    news_id = row.id
    # id_ = row.id
    # print(id_)
    id_list = row.tweet_ids_list
    if len(id_list) > 100:
        id_list = id_list[:99]
    news_url = row.news_url
    title = row.title
    # result = api.statuses_lookup(id_ = id_list)
    df2 = get_all_tweets_single_news_story(row_data = row)
    # print(df2.shape)
    
    df = df.append(df2, ignore_index= True)


df.shape

df.to_csv("politifact_fake_all_data.csv")










###### test of logic 


import numpy as np

x = np.repeat(1, 120)
x = range(324)
x = np.asarray(x)
x.shape
x

len(x)


if len(x) > 100:
    i = len(x) // 100
    print(i)
    
    y = x[:99]
    print(y)
    for j in range(i + 1):
        print(j)
        y = x[j * 100: j * 100 + 99]
        print(y)
        # print(j*100, end=" ")
        # print(j*100+99)





























