'''
FIX id column 

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

'''





import pandas as pd
import tweepy
import json 
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




# 'id', 'news_url', 'title', 'tweet_ids' 

test_data = politifact_fake.iloc[100]
test_tweet_id = test_data.tweet_ids_list[0:20]








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
df_id = test_data.id
id_list = test_data.tweet_ids_list[:99]
news_url = test_data.news_url
title = test_data.title
result = api.statuses_lookup(id_ = test_tweet_id)



def get_all_tweets(id_list = id_list, df_id = df_id, news_url = news_url, title = title):
    # df = pd.DataFrame(columns=["id","username","text"])
    result = api.statuses_lookup(id_ = id_list)
    if len(id_list) > 100:
        id_list = id_list[:99]
    id_list_result = []
    username_list = []
    text_list = []
    df_id_list = []
    news_url_list = []
    title_list = []
    for status in result:
        id_ = status.id
        id_list_result.append(id_)

        username = status.user.screen_name 
        username_list.append(username)

        text = status.text
        text_list.append(text)

        df_id_list.append(df_id)
        news_url_list.append(news_url)
        title_list.append(title)
    data = {"df_id": df_id_list, "news_url": news_url_list, "title": title_list, "id": id_list_result, "username": username_list, "text": text_list}
    return pd.DataFrame(data)

# now traverse the whole data frame and do this for each row ... 
columns=["df_id","news_url","title", "id", "username", "text"]
df = pd.DataFrame()


politifact_fake_test = politifact_fake[:10]
politifact_fake_test



for row in politifact_fake.iterrows():
    row = row[1] # because iterrows() gives us a tuple (index, row) 
    id_ = row.id
    print(id_)
    id_list = row.tweet_ids_list
    if len(id_list) > 100:
        id_list = id_list[:99]
    news_url = row.news_url
    title = row.title
    # result = api.statuses_lookup(id_ = id_list)
    df2 = get_all_tweets(id_list = id_list, df_id = df_id, news_url = news_url, title = title)
    # print(df2.shape)
    
    df = df.append(df2, ignore_index= True)


df.shape

df.to_csv("politifact_fake_all_data.csv")



















