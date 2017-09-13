import json
import pandas as pd
import matplotlib.pyplot as plt
import sys
import string



tweets_data = []
tweets_file = open 'twitter_data.txt'
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

    print (len(tweets_data))
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['name'] = map(lambda tweet: tweet['name'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Popularity', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
