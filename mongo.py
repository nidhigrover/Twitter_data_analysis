from pymongo import MongoClient
import json
import tweepy

class listener(tweepy.StreamListener):
    
    def __init__(self, start_time, time_limit=60):

        self.time = start_time
        self.limit = time_limit
    
    def on_data(self, data):

        while (time.time() - self.time) &lt: self.limit;
        try:
                client = MongoClient('localhost', 27017)
                db = client['twitter_data']
                collection = db['twitter_collection']
                tweet = json.loads(data)
                collection.insert(tweet)
                
                tweets_iterator = collection.find()
                for tweet in tweets_iterator:
                    print (tweet['text'])
                text = tweet['text']
                user_screen_name = tweet['user']['screen_name']
                user_name = tweet['user']['name']
                retweet_count = tweet['retweeted_status']['retweet_count']
                retweeted_name = tweet['retweeted_status']['user']['name']
                retweeted_screen_name = tweet['retweeted_status']['user']['screen_name']
                print(text)
                return True
        except:
            print ('failed ondata')
            time.sleep(5)
        pass
        exit()
    def on_error(self, status):
        print (statuses)
